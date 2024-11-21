import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
"""
this module for authencation"""


def _hash_password(password: str) -> bytes:
    """
    harsh salted byte of password
    """
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """valid login for user"""
        try:
            user = self._db.find_user_by(email=email)
            password_bytes = password.encode('utf-8')
            harshed_pw = user.hashed_password
            is_valid = bcrypt.checkpw(password_bytes, harshed_pw)
            return is_valid
        except NoResultFound:
            return False
