import logging
import subprocess
import json
import os
from flask import send_from_directory
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from create_db import populateDatabase, session

app = Flask(__name__)

def getData(model):
    data = {}

    if model in 'book':
        keys = Book.__table__.columns.keys()
        request = session.query(Book).all()
    elif model in 'author':
        keys = Author.__table__.columns.keys()
        request = session.query(Author).all()
    else:
        keys = Publisher.__table__.columns.keys()
        request = session.query(Publisher).all()

    tableData = []
    for item in request:
        rowData = []
        for key in keys:
            rowData.append(getattr(item, key))
        tableData.append(rowData)

    data['data'] = tableData
    result = json.dumps(data)

    return result



@app.route('/')
def home():
    return render_template('splash.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/<page>/')
def anypage(page):
    if page in 'books':
        columns = Book.__table__.columns.keys()
        return render_template('book_list.html', columns=columns)
    elif page in 'publishers':
        columns = Publisher.__table__.columns.keys()
        return render_template('publisher_list.html', columns=columns)
    elif page in 'authors':
        columns = Author.__table__.columns.keys()
        return render_template('author_list.html', columns=columns)
    return render_template(page+'.html')

@app.route('/_server_data_book')
def get_server_data_book():
    return getData('book')

@app.route('/_server_data_author')
def get_server_data_author():
    return getData('author')

@app.route('/_server_data_publisher')
def get_server_data_publisher():
    return getData('publisher')

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
