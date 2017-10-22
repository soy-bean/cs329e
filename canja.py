import logging

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('Home.html')

@app.route('/stats/')
def stats():
    return render_template('Stats.html')

@app.route('/authorlist/')
def authorlist():
    return render_template('Authorlist.html')

@app.route('/booklist/')
def booklist():
    return render_template('Booklist.html')

@app.route('/publisherlist')
def publisherlist():
    return render_template('Publisherlist.html')

@app.route('/author1')
def author1():
    return render_template('Author1.html')

@app.route('/author2')
def author2():
    return render_template('Author2.html')

@app.route('/author3')
def author3():
    return render_template('Author3.html')

@app.route('/book1')
def book1():
    return render_template('Book1.html')

@app.route('/book2')
def book2():
    return render_template('Book2.html')

@app.route('/book3')
def book3():
    return render_template('Book3.html')

@app.route('/publisher1')
def publisher1():
    return render_template('Publisher1.html')

@app.route('/publisher2')
def publisher2():
    return render_template('Publisher2.html')

@app.route('/publisher3')
def publisher3():
    return render_template('Publisher3.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('Oops, our bad. An error occurred during a request.')
    return """An internal error occurred: <pre>{}</pre>See logs for full stacktrace.""".format(e), 500

if __name__=="__main__":
    app.run()
