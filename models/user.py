#!/usr/bin/python3
"""
class User to handle user info
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, args, **kwargs):
        """initializes User"""
        super().init(args, **kwargs)
