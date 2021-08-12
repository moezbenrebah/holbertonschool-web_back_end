#!/usr/bin/env python3
"""session expiration module"""

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from models.user import User
import os
from os import getenv
import uuid


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""

    def __init__(self):
        """initialization"""

        duration_vrb = os.getenv('SESSION_DURATION')
        try:
            if not duration_vrb:
                self.session_duration = 0
            else:
                self.session_duration = int(duration_vrb)
        except Exception as err:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """create session ID"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """return user ID from a session dictionary"""
        if session_id is None:
            return None
        
        main_dict = self.user_id_by_session_id[session_id]
        
        if session_id not in main_dict.keys():
            return None
        if self.session_duration <= 0:
            return main_dict['user_id']
        if 'created_at' not in main_dict.keys():
            return None

        t = timedelta(seconds=self.session_dictionary) + \
            main_dict['created_at']

        if t < datetime.now():
            return None
        return main_dict['user_id']