# /usr/bin/python3
"""Contains Test cases for the test_city file"""
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestCity(unittest.TestCase):
    """Test for the city class"""

    def test_subclass(self):
        """Test for subclass of BaseModel"""
        place = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """Tests if place has attributes of BaseClass"""
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
