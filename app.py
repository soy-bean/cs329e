import logging
import subprocess
import json
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from create_db import populateDatabase, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('splash.html')

@app.route('/<page>/')
def anypage(page):
    if page == 'books':
        books_old = session.query(Book).all()
        return render_template('book_list.html', books = books_old)
    elif page == 'publishers':
        publishers = session.query(Publisher).distinct(Publisher.name).all()
        return render_template('publisher_list.html', publishers = publishers)
    elif page == 'authors':
        authors = session.query(Author).distinct(Author.name).all()
        return render_template('author_list.html', authors = authors)
    return render_template(page+'.html')

# @app.route('/authors/<name>/')
# def authorpage(name):
#     author = session.query(Authors).filter(Authors.name = name)
#     return render_template('author.html', author = author)

@app.route('/booklist')
def bookList():
    books = session.query(Book).all()
    return render_template('book_list.html', books = books)


@app.route('/unit_tests')
def unit_tests():
  output = subprocess.getoutput("python test.py")
  return json.dumps({'output': str(output)})

@app.route('/book/<int:id_b>')
def book(id_b):
    book = session.query(Book).filter(Book.id == id_b).all()
    return render_template('book.html',book=book)

@app.route('/author/<int:id_a>')
def author(id_a):
    author = session.query(Author).filter(Author.id == id_a).all()
    return render_template('author.html',author=author)

@app.route('/publisher/<int:id_p>')
def publisher(id_p):
    publisher = session.query(Publisher).filter(Publisher.id == id_p).all()
    return render_template('publisher.html',publisher=publisher)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__== "__main__":
    app.run()
