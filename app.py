import logging
import subprocess
import json
import os
from flask import Flask, Response, render_template, request, url_for, send_from_directory, jsonify, redirect, make_response
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
    elif model in 'publisher':
        keys = Publisher.__table__.columns.keys()
        request = session.query(Publisher).all()
    else:
        auto_results = []
        books = session.query(Book).all()
        authors = session.query(Author).all()
        publishers = session.query(Publisher).all()
        for book in books:
            temp = {}
            b_name = getattr(book, 'title')
            temp['value'] = b_name
            temp['label'] = b_name
            auto_results.append(temp)
        for author in authors:
            temp = {}
            a_name = getattr(author, 'name')
            temp['value'] = a_name
            temp['label'] = a_name
            auto_results.append(temp)
        for publisher in publishers:
            temp = {}
            p_name = getattr(publisher, 'name')
            temp['value'] = p_name
            temp['label'] = p_name
            auto_results.append(temp)
        return auto_results

    tableData = []
    for item in request:
        rowData = []
        for key in keys:
            rowData.append(getattr(item, key))
        tableData.append(rowData)

    data['data'] = tableData
    result = json.dumps(data)

    return result

@app.route('/', methods=['GET','POST'])
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
    # book = session.query(Book).filter(Book.id == id_b).all()

    # relations = session.query(Book_Authors_Association).filter(Book_Authors_Association.book == book[0].title).all()
    # publisher = session.query(Publisher).filter(Publisher.name == relations[0].publisher).all()
    # authors = []

    # for relation in relations:
    #     authors.append(relation.author)
    
    # authorsQuery = session.query(Author).filter(Author.name.in_(authors)).all()

    # for thing in authorsQuery:
    #     print(thing.name)

    results = runQueryFor(id_b, "book")
        
    return render_template('book.html', book=results[0], publisher=[1], authors=[2])

@app.route('/author/<int:id_a>')
def author(id_a):
    # author = session.query(Author).filter(Author.id == id_a).all()

    # relations = session.query(Book_Authors_Association).filter(Book_Authors_Association.author == author[0].name).all()
    # publishers = []
    # books = []

    # for relation in relations:
    #     if relation.publisher not in publishers:
    #         publishers.append(relation.publisher)
    #     if relation.book not in books:
    #         books.append(relation.book)
    
    # publishersQuery = session.query(Publisher).filter(Publisher.name.in_(publishers)).all()
    # booksQuery = session.query(Book).filter(Book.title.in_(books)).all()
    results = runQueryFor(id_a, "author")

    return render_template('author.html',author=results[0], publisher=results[1], book=results[2])

@app.route('/publisher/<int:id_p>')
def publisher(id_p):
    # publisher = session.query(Publisher).filter(Publisher.id == id_p).all()

    # relations = session.query(Book_Authors_Association).filter(Book_Authors_Association.publisher == publisher[0].name).all()
    # authors = []
    # books = []

    # for relation in relations:
    #     if relation.author not in authors:
    #         authors.append(relation.author)
    #     if relation.book not in books:
    #         books.append(relation.book)
    
    # authorsQuery = session.query(Author).filter(Author.name.in_(authors)).all()
    # booksQuery = session.query(Book).filter(Book.title.in_(books)).all()

    results = runQueryFor(id_p, "publisher")

    return render_template('publisher.html',publisher=results[0], author=results[1], book=results[2])

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	search = request.args.get('q')
	results = getData('auto')
	return jsonify(matching_results=results)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


def runQueryFor(instanceOf, entity):

    output = []

    if (entity == "author"):

        author = session.query(Author).filter(Author.id == instanceOf).all()
        output.append(author)

        relations = session.query(Book_Authors_Association).filter(Book_Authors_Association.author == author[0].name).all()
        publishers = []
        books = []

        for relation in relations:
            if relation.publisher not in publishers:
                publishers.append(relation.publisher)
            if relation.book not in books:
                books.append(relation.book)
        
        publishersQuery = session.query(Publisher).filter(Publisher.name.in_(publishers)).all()
        booksQuery = session.query(Book).filter(Book.title.in_(books)).all()

        output.append(publishersQuery)
        output.append(booksQuery)

        return output
    
    elif (entity == "publisher"):

        publisher = session.query(Publisher).filter(Publisher.id == instanceOf).all()
        output.append(publisher)

        relations = session.query(Book_Authors_Association).filter(Book_Authors_Association.publisher == publisher[0].name).all()
        authors = []
        books = []

        for relation in relations:
            if relation.author not in authors:
                authors.append(relation.author)
            if relation.book not in books:
                books.append(relation.book)
        
        authorsQuery = session.query(Author).filter(Author.name.in_(authors)).all()
        booksQuery = session.query(Book).filter(Book.title.in_(books)).all()

        output.append(authorsQuery)
        output.append(booksQuery)

        return output
    
    elif (entity == "book"):

        book = session.query(Book).filter(Book.id == instanceOf).all()

        relations = session.query(Book_Authors_Association).filter(Book_Authors_Association.book == book[0].title).all()
        publisher = session.query(Publisher).filter(Publisher.name == relations[0].publisher).all()
        authors = []

        for relation in relations:
            authors.append(relation.author)
        
        authorsQuery = session.query(Author).filter(Author.name.in_(authors)).all()

        output.append(book)
        output.append(publisher)
        output.append(authorsQuery)

        return output

if __name__== "__main__":
    app.run()
