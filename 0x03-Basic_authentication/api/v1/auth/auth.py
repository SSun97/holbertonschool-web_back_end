from flask import request
from typing import List, TypeVar

class Auth:
    """ class for authorization """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method return False """
        return False

    def authorization_header(self, request=None) -> str: 
        """ Public method return None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method returns None """
        return None