import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    __searchable__ = ['name','education','nationality']
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    born = Column(String())
    education = Column(String())
    nationality = Column(String())
    alma_mater = Column(String())
    description = Column(String())
    wikipedia_url = Column(String())
    died = Column(String())
    image_url = Column(String())

class Publisher(Base):
    __tablename__ = 'publishers'
    __searchable__ = ['name']
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    founded=Column(String())
    location=Column(String())
    wiki_link = Column(String())
    description = Column(String())
    owner = Column(String())
    image_url = Column(String())
    website = Column(String())

class Book(Base):
    __tablename__ = 'book'
    __searchable__ = ['title','isbn']
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    subtitle = Column(String())
    google_id = Column(String())
    isbn = Column(String())
    pub_date = Column(String())
    image_url = Column(String())
    description = Column(String())

class Book_Authors_Association(Base):
    __tablename__ = 'book_author_association'
    id_b_p_a = Column(Integer, primary_key=True)
    book = Column(String())
    publisher = Column(String())
    author = Column(String())

# Change postgresql://postgres:asd123@localhost/---->postgres<---- to the name of the database you give to your local system
# postgresql://DB_USER:PASSWORD@HOST/DATABASE
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:asd123@localhost/postgres')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# try to run this file:
# python create_db.py
