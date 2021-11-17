#!/usr/bin/env python3
""" User passwords should NEVER be stored in plain text in a database """
import bcrypt


def hash_password(password: str) -> bytes:
    """ function that expects one string argument and returns
    a salted, hashed password, which is a byte string"""
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())
