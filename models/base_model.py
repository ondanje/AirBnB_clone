#!/usr/bin/python3
"""
BaseModel class that defines all common
attributes/methods for other classes:
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Initializes the base model"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("updated_at", "created_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "id":
                    try:
                        """convert to a string"""
                        value = str(value)
                        value = uuid.UUID(value)
                    except ValueError:
                        value = uuid.UUID(hex=value)
                setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute to saved time
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all keys and values
        """
        dictionary = {}

        dictionary["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                value = value.isoformat()

            dictionary[key] = value
        return dictionary
