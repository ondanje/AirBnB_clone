#!/usr/bin/python3
"""
class Review to handle reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
