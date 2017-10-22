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
        result = self.app.get('/stats/')
        self.assertEqual(result.status_code, 200)

    def test_authorlist_status_code(self):
        result = self.app.get('/authorlist/')
        self.assertEqual(result.status_code, 200)

    def test_booklist_status_code(self):
        result = self.app.get('/booklist/')
        self.assertEqual(result.status_code, 200)

    def test_publisherlist_status_code(self):
        result = self.app.get('/publisherlist/')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
  unittest.main()
