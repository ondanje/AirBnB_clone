# /usr/bin/python3
"""Contains Test cases for the test_city file"""
from datetime import datetime
from models import city
from models.base_model import BaseModel
import unittest

City = city.City


class TestCity(unittest.TestCase):
    """Test for the city class"""

    def test_class(self):
        """Test for instance of City"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Tests if CIty has attributes of BaseClass"""
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
