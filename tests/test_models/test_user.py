from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Class to test test_user"""

    def test_user_instance(self):
        """Test that user is isntance of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attr(self):
        """Test that User class has attributes"""
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
