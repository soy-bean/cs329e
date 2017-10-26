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

    def test_not_found_status_code(self):
        result = self.app.get('www.reddit.com/r/flask')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
  unittest.main()
