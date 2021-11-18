#!/usr/bin/env python3
"""
bcrypt example
"""
import bcrypt


password = "MyAmazingPassw0rd"


def hash_password(password: str) -> bytes:
    """ function that expects one string argument and returns
    a salted, hashed password, which is a byte string"""
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())


print(hash_password(password))
print(hash_password(password))
