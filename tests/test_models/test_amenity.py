# /usr/bin/python3
"""Contains Test cases for the test_city file"""
from datetime import datetime
from models.base_model import BaseModel
from models import amenity
import unittest

Amenity = amenity.Amenity


class TestCity(unittest.TestCase):
    """Test for the city class"""

    def test_subclass(self):
        """Test for subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Tests if Amenity has attributes of BaseClass"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
