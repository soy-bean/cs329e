import json, logging
from sqlalchemy.orm import sessionmaker
from models import *

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

    for oneBook in books:
        google_id = oneBook['google_id']
        title = oneBook['title']
        isbn = oneBook.get('isbn')
        publication_date = oneBook.get('publication_date')
        image_url = oneBook['image_url']
        description = oneBook.get('description')

        newBook = Book(title=title,
                       google_id=google_id,
                       isbn=isbn,
                       pub_date=publication_date,
                       image_url=image_url,
                       description=description)

        session.add(newBook)

        for publisher in oneBook['publishers']:
            p_wiki_link = publisher.get('wikipedia_url')
            p_name = publisher.get('name')
            p_description = publisher.get('description')
            p_owner = publisher.get('owner')
            p_image_url = publisher.get('image_url')
            p_website = publisher.get('website')

            newPublisher = Publisher(wiki_link=p_wiki_link,
                                     name=p_name,
                                     description=p_description,
                                     owner=p_owner,
                                     image_url=p_image_url,
                                     website=p_website)
            session.add(newPublisher)

        for author in oneBook['authors']:
            a_birth = author.get('born')
            a_name = author.get('name')
            a_education = author.get('education')
            a_nationality = author.get('nationality')
            a_alma_mater = author.get('alma_mater')
            a_wiki_link = author.get('wikipedia_url')
            a_image_url = author.get('image_url')

            newAuthor = Author(name=a_name,
                               birth=a_birth,
                               education=a_education,
                               nationality=a_nationality,
                               alma_mater=a_alma_mater,
                               wiki_link=a_wiki_link,
                               image_url=a_image_url, )
            session.add(newAuthor)

            book_author_pub = Book_Authors_Association(book=newBook, author=newAuthor, publisher=newPublisher)
            session.add(book_author_pub)

        session.commit()


create_books()