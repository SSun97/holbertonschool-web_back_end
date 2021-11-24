#!/usr/bin/env python3
"""
SessionAuth module for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ SessionAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a session
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User ID from Session ID
            Return a User ID based on a Session ID
        """
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)