import os
import unittest
from flask import Flask,render_template
from models import Base, Book, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import app

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class MyTestClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_stats_status_code(self):
        result = self.app.get('/about/')
        self.assertEqual(result.status_code, 200)

    def test_book1_status_code(self):
        result = self.app.get('/book/1')
        self.assertEqual(result.status_code, 200)

    def test_book2_status_code(self):
        result = self.app.get('/book/2')
        self.assertEqual(result.status_code, 200)

    def test_book3_status_code(self):
        result = self.app.get('/book/3')
        self.assertEqual(result.status_code, 200)

    def test_author1_status_code(self):
        result = self.app.get('/author/1')
        self.assertEqual(result.status_code, 200)

    def test_author2_status_code(self):
        result = self.app.get('/author/2')
        self.assertEqual(result.status_code, 200)

    def test_author3_status_code(self):
        result = self.app.get('/author/3')
        self.assertEqual(result.status_code, 200)

    def test_publisher1_status_code(self):
        result = self.app.get('/publisher/1')
        self.assertEqual(result.status_code, 200)

    def test_publisher2_status_code(self):
        result = self.app.get('/publisher/2')
        self.assertEqual(result.status_code, 200)

    def test_publisher3_status_code(self):
        result = self.app.get('/publisher/3')
        self.assertEqual(result.status_code, 200)

    def test_not_found_status_code(self):
        result = self.app.get('www.reddit.com/r/flask')
        self.assertEqual(result.status_code, 404)

    def test_source_insert_1(self):
        s = Book(id='20000', title = 'C++')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '20000').one()
        self.assertEqual(str(r.id), '20000')

        session.query(Book).filter_by(id = '20000').delete()
        session.commit()

    def test_source_insert_2(self):
        s = Book(id='20001', title = 'Ruby on Rails')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '20001').one()
        self.assertEqual(str(r.id), '20001')

        session.query(Book).filter_by(id = '20001').delete()
        session.commit()

    def test_source_insert_3(self):
        s = Book(id='20002', title = 'Erlang')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '20002').one()
        self.assertEqual(str(r.id), '20002')

        session.query(Book).filter_by(id = '20002').delete()
        session.commit()


if __name__ == '__main__':
  unittest.main()
