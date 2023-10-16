#!/usr/bin/python3
"""
Console containing the entry point of command interpreter
"""
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
        "State": State,
    }

    def do_EOF(self, line):
        """
        Exit the program (ctrl +D)
        """
        return True

    def do_quit(self, line):
        """
        Exit the program
        """
        return True

    def emptyline(self):
        """
        command that does nothing when an empty line is entered
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        command = line.split()
        if not command:
            print(f"** class name missing **")
            return
        else:
            if command[0] not in self.dictionary.keys():
                print(f"** class doesn't exist **")
                return
            new_inst = self.dictionary[command[0]]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, line):
        """
        command to display specific instances
        """
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
        """
        command to delete specific instances
        """
        command = line.split()

        if not command:
            print("** class name missing **")
        elif command[0] not in self.dictionary.keys():
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        else:
            key_instance = "{}.{}".format(command[0], command[1])
            inst_storage = storage.all()
            if key_instance in inst_storage:
                del inst_storage[key_instance]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        command = line.split()

        if not command:
            print(storage.all())

        else:
            class_name = command[0]

            if class_name not in self.dictionary.keys():
                print("** class doesn't exist **")
                return

            if len(command) == 1:
                instances = storage.all()
                class_instances = [
                    str(instance)
                    for instance in instances.values()
                    if instance.__class__.__name__ == class_name
                ]
                print(class_instances)
            else:
                instance_key = "{}.{}".format(class_name, command[1])
                instances = storage.all()
                if instance_key in instances:
                    print(instances[instance_key])

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        Usage:update <class name> <id> <attribute name> "<attribute value>"
        """
        command = line.split()

        if not command:
            print("** class name missing **")
            return

        class_name = command[0]

        if class_name not in self.dictionary.keys():
            print("** class doesn't exist **")
            return

        if len(command) < 2:
            print("** instance id missing **")
            return

        instance_key = "{}.{}".format(class_name, command[1])
        instances = storage.all()

        if instance_key in instances:
            if len(command) < 3:
                print("** attribute name missing **")
            elif len(command) < 4:
                print("** value missing **")
                return

            attr_name = command[2]
            value = command[3]

            instance = instances[instance_key]
            if attr_name not in ["id", "created_at", "updated_at"]:
                setattr(instance, attr_name, value)
                instance.save()
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
