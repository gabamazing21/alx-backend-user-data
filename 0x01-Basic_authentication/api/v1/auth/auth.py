#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar
from models.user import User
"""
This module deals with api authentication
"""


class Auth():
    """
    this class enable auth method
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        False - path
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        normalized_path = path.rstrip('/')

        for exclude_path in excluded_paths:
            if normalized_path == exclude_path.rstrip('/'):
                return False
            return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request will be the Flask request object
        """
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
         that returns None - request will be the Flask request object
        """
        return None
