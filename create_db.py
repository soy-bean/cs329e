import json, logging
from sqlalchemy.orm import sessionmaker
from models import Base, Book, engine


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_books():
    books = load_json('books.json')

    id = 1
    for oneBook in books:
        # google_id = oneBook['google_id']
        title = oneBook['title']
        # isbn = oneBook['isbn']
        # publication_date = oneBook['publication_date']
        # image_url = oneBook['image_url']
        # description = oneBook['description']
        # publishers = oneBook['publishers']
        # authors = oneBook['authors']

        newBook = Book(title=title, id=id)
        session.add(newBook)
        session.commit()
        id += 1


create_books()