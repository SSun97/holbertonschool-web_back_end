#!/usr/bin/env python3
""" auth file """
from flask import request
from typing import List, TypeVar
from os import getenv
from models.user import User


class Auth:
    """ class for authorization """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require authorithation """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def session_cookie(self, request=None):
        """ returns a cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))

    def authorization_header(self, request=None) -> str:
        """ Public method return None """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method returns None """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        try:
            return User.get(id=user_id)
        except KeyError:
            return None
