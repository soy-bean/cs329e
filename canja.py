import logging

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def spalsh():
    return render_template('home.html')

@app.route('/stats.html/')
def stats():
    return render_template('stats.html')

@app.route('/view.html/')
def views():
    return render_template('view.html')

@app.route('/view.html/authorlist.html')
def authorlist():
    return render_template('authorlist.html')

@app.route('/view.html/booklist.html/')
def booklist():
    return render_template('booklist.html')

@app.route('/view.html/publisherlist.html/')
def publisherlist():
    return render_template('publisherlist.html')

@app.route('/view.html/author1.html')
def author1():
    return render_template('author1.html')

@app.route('/view.html/author2.html')
def author2():
    return render_template('author2.html')

@app.route('/view.html/author3.html')
def author3():
    return render_template('author3.html')

@app.route('/view.html/booklist.html/book1.html')
def book1():
    return render_template('book1.html')

@app.route('/view.html/booklist.html/book2.html')
def book2():
    return render_template('book2.html')

@app.route('/view.html/booklist.html/book3.html')
def book3():
    return render_template('book3.html')

@app.route('/view.html/publisherlist.html/publisher1.html')
def publisher1():
    return render_template('publisher1.html')

@app.route('/view.html/publisherlist.html/publisher2.html')
def publisher2():
    return render_template('publisher2.html')

@app.route('/view.html/publisherlist.html/publisher3.html')
def publisher3():
    return render_template('publisher3.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('Oops, our bad. An error occurred during a request.')
    return """An internal error occurred: <pre>{}</pre>See logs for full stacktrace.""".format(e), 500

if __name__=="__main__":
    app.run()
