import unittest
from flask import Flask,render_template

from canja import app


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


if __name__ == '__main__':
  unittest.main()
