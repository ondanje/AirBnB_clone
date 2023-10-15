import unittest
from models import review
from datetime import datetime
from models.base_model import BaseModel

# /usr/bin/python3
"""Contains Test cases for the test_city file"""
from datetime import datetime
from models.base_model import BaseModel
from models import state
import unittest

Review = review.Review


class TestCity(unittest.TestCase):
    """Test for the city class"""

    def test_subclass(self):
        """Test for subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Tests if State has attributes of BaseClass"""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
