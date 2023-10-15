#!/usr/bin/python3
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os


class FileStorage:
    """To handle storage of a file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_data = {}

        for key, obj in FileStorage.__objects.items():
            serialized_data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for values in data.values():
                    cls_name = values["__class__"]
                    self.new(eval(cls_name)(**values))
