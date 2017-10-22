import logging

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/stats/')
def stats():
    return render_template('stats.html')

@app.route('/authorlist/')
def authorlist():
    return render_template('authorlist.html')

@app.route('/booklist/')
def booklist():
    return render_template('booklist.html')

@app.route('/publisherlist/')
def publisherlist():
    return render_template('publisherlist.html')

@app.route('/author1/')
def author1():
    return render_template('author1.html')

@app.route('/author2/')
def author2():
    return render_template('author2.html')

@app.route('/author3/')
def author3():
    return render_template('author3.html')

@app.route('/book1/')
def book1():
    return render_template('book1.html')

@app.route('/book2/')
def book2():
    return render_template('book2.html')

@app.route('/book3/')
def book3():
    return render_template('book3.html')

@app.route('/publisher1/')
def publisher1():
    return render_template('publisher1.html')

@app.route('/publisher2/')
def publisher2():
    return render_template('publisher2.html')

@app.route('/publisher3/')
def publisher3():
    return render_template('publisher3.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('Oops, our bad. An error occurred during a request.')
    return """An internal error occurred: <pre>{}</pre>See logs for full stacktrace.""".format(e), 500

if __name__=="__main__":
    app.run()
