import bcrypt
"""
this module for authencation"""


def _hash_password(password: str) -> bytes:
    """
    harsh salted byte of password
    """
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password
