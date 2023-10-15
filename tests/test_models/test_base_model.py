# /usr/bin/python3
"""Contains Test cases for the test_city file"""
from datetime import datetime
from models.base_model import BaseModel
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Test for the city class"""

    def test_attributes(self):
        """Tests if base_model has attributes of BaseClass"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"))
        self.assertTrue(hasattr(base_model, "created_at"))
        self.assertTrue(hasattr(base_model, "updated_at"))
