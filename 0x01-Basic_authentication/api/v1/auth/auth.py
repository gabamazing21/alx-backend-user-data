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
        return False 
    
    def authorization_header(self, request=None) -> str:
        """
        returns None - request will be the Flask request object
        """
        return request
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
         that returns None - request will be the Flask request object
        """
        return request