#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Console.py command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program (ctrl +D)"""
        return True

    def do_quit(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
