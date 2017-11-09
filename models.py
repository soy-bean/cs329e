import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    birth = Column(String())
    education = Column(String())
    nationality = Column(String())
    alma_mater = Column(String())
    wiki_link = Column(String())
    image_url = Column(String())
    books = relationship('Book', secondary='book_author_association')

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    wiki_link = Column(String())
    description = Column(String())
    owner = Column(String())
    image_url = Column(String())
    website = Column(String())

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    google_id = Column(String())
    isbn = Column(String())
    pub_date = Column(String())
    image_url = Column(String())
    description = Column(String())
    authors = relationship('Author', secondary='book_author_association')
    publisher = relationship('Publisher', secondary='book_author_association')

class Book_Authors_Association(Base):
    __tablename__ = 'book_author_association'
    id_book = Column(Integer, ForeignKey('book.id'), primary_key=True)
    id_author = Column(Integer, ForeignKey('authors.id'), primary_key=True)
    id_publisher = Column(Integer, ForeignKey('publishers.id'), primary_key=True)
    book = relationship(Book, backref=backref("author_assoc"))
    author = relationship(Author, backref=backref("book_assoc"))
    publisher = relationship(Publisher, backref=backref("publisher_assoc"))

# Change postgresql://postgres:asd123@localhost/---->postgres<---- to the name of the database you give to your local system
# postgresql://DB_USER:PASSWORD@HOST/DATABASE
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:password@/idbcs329e?host=/cloudsql/cs329-184115:us-central1:idbcs329e')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# try to run this file:
# python create_db.py
