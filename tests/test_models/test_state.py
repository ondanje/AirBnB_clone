# /usr/bin/python3
"""Contains Test cases for the test_city file"""
from datetime import datetime
from models.base_model import BaseModel
from models import state
import unittest

State = state.State


class TestCity(unittest.TestCase):
    """Test for the city class"""

    def test_subclass(self):
        """Test for subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Tests if State has attributes of BaseClass"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
