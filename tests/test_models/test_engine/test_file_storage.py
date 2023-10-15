#!/usr/bin/python3
"""
TestFileStorage Classes
"""

from datetime import datetime
import inspect
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import unittest

FileStorage = file_storage.FileStorage
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class TestFileStorageDocs(unittest.TestCase):
    """Checking for correct documentation"""

    @classmethod
    def setUpClass(cls):
        """Setter for the doc"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_file_storage_docstring(self):
        """TFile storage docstring"""
        self.assertIsNot(
            file_storage.__doc__, None, "file_storage.py requires docstring"
        )
        self.assertTrue(
            len(file_storage.__doc__) >= 1,
            "file_storage.py requires docstring"
        )

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage  docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "State class requires docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "State class requires docstring")

    def test_docstrings(self):
        """Docstring presence test"""
        for func in self.fs_f:
            self.assertIsNot(
                func[1].__doc__, None,
                "{:s} method requires docstring".format(func[0])
            )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method requires docstring".format(func[0]),
            )


class TestFileStorage(unittest.TestCase):
    """FileStorage Test"""

    def test_all_returns_dict(self):
        """Test all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dictionary = storage.all()
        self.assertEqual(type(new_dictionary), dict)
        self.assertIs(new_dictionary, storage._FileStorage__objects)

    def test_new(self):
        """test that new adds an object"""
        storage = FileStorage()
        save_str = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dictionary = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dictionary[instance_key] = instance
                self.assertEqual(test_dictionary,
                                 storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save_str

    def test_save(self):
        """Test that save properly saves objects"""
        os.remove("file.json")
        storage = FileStorage()
        new_dictionary = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dictionary[instance_key] = instance
        save_str = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dictionary
        storage.save()
        FileStorage._FileStorage__objects = save_str
        for key, value in new_dictionary.items():
            new_dictionary[key] = value.to_dict()
        string = json.dumps(new_dictionary)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
