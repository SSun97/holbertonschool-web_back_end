#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user and commit to DB """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ Find user by email. Query.one() requires that there is only one
        result in the result set; it is an error if the database returns 0
        or 2 or more results and an exception will be raised. Query.first()
        returns the first of a potentially larger result set (adding LIMIT 1
        to the query), or None if there were no results. No exception will
        be raised.
        """
        results = self._session.query(User).filter_by(**kwargs)
        return results.one()

    def update_user(self, user_id: int, **kwargs: dict):
        """ find user and update password """
        user = self.find_user_by(id=user_id)
        for key in kwargs.keys():
            if key not in list(user.__dict__.keys()):
                raise ValueError
        for key, value in kwargs.items():
            setattr(user, key, value)
        self._session.add(user)
        self._session.commit()
