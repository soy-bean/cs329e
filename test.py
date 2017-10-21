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

    # def test_home_data(self):
    #     # sends HTTP GET request to the application
    #     # on the specified path
    #     result = self.app.get('/')
    #
    #     # assert the response data
    #     self.assertEqual(result.data, render_template('home.html'))


if __name__ == '__main__':
  unittest.main()
