import logging
import subprocess
import json
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from create_db import create_books, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('splash.html')

@app.route('/<page>/')
def anypage(page):
    if page == 'books':
        books = session.query(Book).all()
        return render_template('book_list.html', books = books)
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
<<<<<<< HEAD
    if id_b == 1:
        content = {
                "id_b":"1",
                "cover":"https://books.google.com/books/content/images/frontcover/wrOQLV6xB-wC?fife=w500",
                "title":"Harry Potter and the Sorcerer's Stone",
                "description":"Turning the envelope over, his hand trembling, Harry saw a purple wax seal bearing a coat of arms; a lion, an eagle, a badger and a snake surrounding a large letter 'H'. Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry's eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure is about to begin!",
                "googleid":"wrOQLV6xB-wC",
                "isbn":"9781781100486",
                "pubdate":"2015-12-08"
        }
        return render_template('book.html',**content)
    elif id_b == 2:
        content = {
                "id_b":"2",
                "cover":"https://books.google.com/books/content/images/frontcover/Y-41Q9zk32kC?fife=w500",
                "title":"The Well of Ascension",
                "description":"From #1 New York Times bestselling author Brandon Sanderson, the Mistborn series is a heist story of political intrigue and magical, martial-arts action. The impossible has been accomplished. The Lord Ruler -- the man who claimed to be god incarnate and brutally ruled the world for a thousand years -- has been vanquished. But Kelsier, the hero who masterminded that triumph, is dead too, and now the awesome task of building a new world has been left to his young protege, Vin, the former street urchin who is now the most powerful Mistborn in the land, and to the idealistic young nobleman she loves. As Kelsier's protege and slayer of the Lord Ruler she is now venerated by a budding new religion, a distinction that makes her intensely uncomfortable. Even more worrying, the mists have begun behaving strangely since the Lord Ruler died, and seem to harbor a strange vaporous entity that haunts her. Stopping assassins may keep Vin's Mistborn skills sharp, but it's the least of her problems. Luthadel, the largest city of the former empire, doesn't run itself, and Vin and the other members of Kelsier's crew, who lead the revolution, must learn a whole new set of practical and political skills to help. It certainly won't get easier with three armies, one of them composed of ferocious giants now vying to conquer the city, and no sign of the Lord Ruler's hidden cache of atium, the rarest and most powerful allomantic metal. As the siege of Luthadel tightens, an ancient legend seems to offer a glimmer of hope. But even if it really exists, no one knows where to find the Well of Ascension or what manner of power it bestows. The Cosmere The Mistborn series Mistborn: The Final Empire The Well of Ascension The Hero of Ages Alloy of Law Shadows of Self Bands of Mourning The Stormlight Archive The Way of Kings Words of Radiance Edgedancer (Novella) Oathbringer (forthcoming) Collection Arcanum Unbounded Other Cosmere Titles Elantris Warbreaker Rithmatist The Alcatraz vs. the Evil Librarians series Alcatraz vs. the Evil Librarians The Scrivener's Bones The Knights of Crystallia The Shattered Lens The Dark Talent The Reckoners Steelheart Firefight Calamity At the Publisher's request, this title is being sold without Digital Rights Management Software (DRM) applied.",
                "googleid":"Y-41Q9zk32kC",
                "isbn":"1429961813",
                "pubdate":"2010-04-01"
        }
        
        return render_template('book.html',**content)
    else:
        content = {
                "id_b":"3",
                "cover":"https://books.google.com/books/content/images/frontcover/dLo_GyEykjQC?fife=w500",
                "title":"The Wise Man's Fear",
                "description":"There are three things all wise men fear: the sea in storm, a night with no moon, and the anger of a gentle man.My name is Kvothe. You may have heard of me. So begins the tale of a hero told from his own point of view a story unequaled in fantasy literature. Now in The Wise Man's Fear, Day Two of The Kingkiller Chronicle, Kvothe takes his first steps on the path of the hero and learns how difficult life can be when a man becomes a legend in his own time.",
                "googleid":"dLo_GyEykjQC",
                "isbn":"1101486406",
                "pubdate":"2011-03-01"
        }
        return render_template('book.html',**content)
=======
    book = session.query(Book).filter(Book.id == id_b).all()
    return render_template('book.html',book=book)
>>>>>>> f3d8a9f96c5631abf4f268533a2f742a17ab13a6

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
