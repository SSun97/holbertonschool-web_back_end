#!/usr/bin/env python3
""" define a _hash_password method that takes in a password string arguments
and returns bytes. """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ bcrypt returns a different hash each time because it incorporates
    a different random value into the hash. This is known as a "salt". """
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email, password) -> User:
        """ register user """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
        else:
            raise ValueError("User {} already exists".format(email))
