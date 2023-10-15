#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console.py command interpreter"""

    prompt = "(hbnb) "
    dictionary = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def do_EOF(self, line):
        """Exit the program (ctrl +D)"""
        return True

    def do_quit(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """
           Creates a new instance of BaseModel,
           saves it (to the JSON file) and prints the id
        """
        command = line.split()
        if not command:
            print(f"** class name is mising **")
            return
        else:
            if command[0] not in self.dictionary.keys():
                print(f"** class does not exist **")
                return
            new_inst = self.dictionary[command[0]]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, line):
        command = line.split()

        if not command:
            print("** class name missing **")
        elif command[0] not in self.dictionary.keys():
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id is missing **")
        else:
            key_instance = "{}.{}".format(command[0], command[1])
            if key_instance in storage.all():
                print(storage.all()[key_instance])
                storage.save()

    def do_destroy(self, line):
        command = line.split()

        if not command:
            print("** class name missing **")
        elif command[0] not in self.dictionary.keys():
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id is missing **")
        else:
            key_instance = "{}.{}".format(command[0], command[1])
            inst_storage = storage.all()
            if key_instance in inst_storage:
                del inst_storage[key_instance]
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
