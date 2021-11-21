#!/usr/bin/env python3
""" Create a class BasicAuth that inherits from Auth """

from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
import re
from base64 import b64decode
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth method """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Base64 method """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

    # def is_base64(str):
    #     """ validate string """
    #     expression = "^([A-Za-z0-9+/]{4})*\
    # ([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$"

    #     matches = re.match(expression, str)

    #     if matches:
    #         return True
    #     else:
    #         return False

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """ Decode Base64 method """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        # if not self.is_base64(base64_authorization_header):
        #     return None
        try:
            baseEncode = base64_authorization_header.encode('utf-8')
            baseDecode = b64decode(baseEncode)
            decodedValue = baseDecode.decode('utf-8')
            return decodedValue
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """ User credentials """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ User Object """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            None
