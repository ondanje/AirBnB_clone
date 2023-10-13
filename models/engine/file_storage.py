#!/usr/bin/python3
import json



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
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                for key, value in data.items():
                    """splits the key into class name & obj id"""
                    class_name, obj_id = key.split(".")
                    obj_dict = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj_dict

        except FileNotFoundError:
            pass
