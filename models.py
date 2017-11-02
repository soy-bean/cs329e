import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Book_Author_Junction = Table('book', Base.metadata,
#     Column('author_id', Integer, ForeignKey('authors.id')),
#     Column('publisher_id', Integer, ForeignKey('publishers.id'))
# )
#
# class Author(Base):
#     __tablename__ = 'authors'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), nullable=False)
#
# class Publisher(Base):
#     __tablename__ = 'publishers'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), nullable=False)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)

# Change postgresql://postgres:asd123@localhost/---->postgres<---- to the name of the database you give to your local system
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:asd123@localhost/postgres')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# try to run this file:
# python create_db.py