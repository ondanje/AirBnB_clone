from datetime import datetime
import uuid


class BaseModel:
    """Initializes the base model"""

    def __init__(self, *args, **kwargs):
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue  # Skip the __class__ key
                if key in ("updated_at", "created_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "id":
                    try:
                        value = str(value)  # Convert to string
                        value = uuid.UUID(value)  # Try to convert to UUID
                    except ValueError:
                        value = uuid.UUID(hex=value)  # Handle non-hexadecimal UUID
                setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.id = uuid.uuid4()

    def __str__(self):
        """Returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute to saved time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of all keys and values"""
        dictionary = {}
        dictionary["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                value = value.isoformat()
            dictionary[key] = value
        return dictionary


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print(
            "\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key])
        )

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
