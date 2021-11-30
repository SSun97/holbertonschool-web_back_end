#!/usr/bin/env python3
""" create a SQLAlchemy model named User for a database table named
users (by using the mapping declaration of SQLAlchemy). """

# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# engine = create_engine('sqlite:///:memory:', echo=False)
Base = declarative_base()


class User(Base):
    """ User class inherites from Base """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_password = Column(String(250))
    session_id = Column(String(250))
    reset_token = Column(String(250))
