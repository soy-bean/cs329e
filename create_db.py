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


'''
Publisher cache functions
'''
def publisherCache(f):

    pub_cache = {}

    def pubDecFunc(founded=None,name=None,location=None,wikipedia_url=None,description=None,website=None,owner=None,image_url=None,**kwargs):
        if name not in pub_cache:
            pub_cache[name] = f(founded,name,location,wikipedia_url,description,website,owner,image_url)
            return pub_cache[name]
        else:
            return pub_cache[name]

    return pubDecFunc

@publisherCache
def popPublisher(founded=None,name=None,location=None,wikipedia_url=None,description=None,website=None,owner=None,image_url=None):
    newPublisher = Publisher(
                                    founded=founded,
                                    wiki_link=wikipedia_url,
                                    location=location,
                                    name=name,
                                    description=description,
                                    website=website,
                                    owner=owner,
                                    image_url=image_url
                            )
    session.add(newPublisher)
    return name


'''
Author Cache functions
'''

def authorCache(f):

    auth_cache = {}

    def authDecFunc(name=None,education=None,nationality=None,alma_mater=None,image_url=None,born=None,description=None,wikipedia_url=None,died=None):
        if name not in auth_cache:
            auth_cache[name] = f(name,education,nationality,alma_mater,image_url,born,description,wikipedia_url,died)
            return auth_cache[name]
        else:
            return auth_cache[name]

    return authDecFunc

@authorCache
def popAuthor(name=None,education=None,nationality=None,alma_mater=None,image_url=None,born=None,description=None,wikipedia_url=None,died=None):
    newAuthor = Author(
                        name=name,
                        education=education,
                        nationality=nationality,
                        alma_mater=alma_mater,
                        image_url=image_url,
                        born=born,
                        description=description,
                        wikipedia_url=wikipedia_url,
                        died=died
                    )
    session.add(newAuthor)
    return name

def getBook(google_id=None,title=None,isbn=None,publication_date=None,image_url=None,description=None,publishers=None,authors=None,subtitle=None):

    row = Book(
                   title=title,
                   subtitle=subtitle,
                   google_id=google_id,
                   isbn=isbn,
                   pub_date=publication_date,
                   image_url=image_url,
                   description=description
               )

    publisher_names = []
    for publisher in publishers:
        publisher_name = popPublisher(**publisher)
        if publisher_name:
            publisher_names.append(publisher_name)

    author_names = []
    for author in authors:
        author_name = popAuthor(**author)
        if author_name:
            author_names.append(author_name)

    for p_n in publisher_names:
        for a_n in author_names:
            session.add(Book_Authors_Association(book=title, author=a_n, publisher=p_n))

    return row

def populateDatabase():
    books = load_json('books.json')

    for oneBook in books:
        newBook = getBook(**oneBook)
        session.add(newBook)

        session.commit()




populateDatabase()