#!/usr/bin/env python3
""" auth file """
from flask import request
from typing import List, TypeVar


class Auth:
    """ class for authorization """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method return False """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if i.endswith('/api/v1/status/'):
                return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Public method return None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method returns None """
        return None
