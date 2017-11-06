import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


Book_Author_Junction = Table('book_author', Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('book_id', Integer, ForeignKey('book.id'))
)

Author_Publisher_Junction = Table('author_publisher', Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('publisher_id', Integer, ForeignKey('publisher.id'))
)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    birth = Column(String(80))
    education = Column(String(80))
    nationality = Column(String(80))
    alma_mater = Column(String(80))
    wiki_link = Column(String(80))
    image_url = Column(String(80))

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    wiki_link = Column(String(80))
    description = Column(String('max'))
    owner = Column(String(80))
    image_url = Column(String(80))
    website = Column(String(80))

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    google_id = Column(String(80), nullable=False)
    isbn = Column(String(80), nullable=False)
    pub_date = Column(String(80))
    image_url = Column(String(80))
    description = Column(String('max'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    publisher = relationship("Publisher")



# Change postgresql://postgres:asd123@localhost/---->postgres<---- to the name of the database you give to your local system
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:asd123@localhost/postgres')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# try to run this file:
# python create_db.py