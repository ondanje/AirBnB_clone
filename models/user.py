#!/usr/bin/python3
"""
class User to handle user info
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes User"""
        super().__init__(*args, **kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""
