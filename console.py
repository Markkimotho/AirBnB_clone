#!/usr/bin/python3

""" Module that for creating our CLI for the AirBnB Clone App"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """class HBNBCommand
    """
    prompt = '(hbnb) '
    

    is_classes = ["BaseModel", "User"]

    def do_quit(self, arg):
        """ Quits the Terminal """
        sys.exit()

    def do_EOF(self, arg):
        """ Defines the EOF:
        ->End of The Program
        ->Quits The Program/Terminal
        ---similar to quit()---
        """
        return True

    def emptyline(self):
        """ Nothing is executed on  emptyline+ENTER """
        pass
        
    def do_create(self, arg):
        """ Creates new instance of class BaseModel """
        if arg == "" or arg is None:
            print("** class name is missing **")
        elif arg not in HBNBCommand.is_classes:
            print("** class doesn't exist **")
            return
    def show(self, arg):
        pass

    def destroy(self, arg):
        pass

    def all(self, arg):
        pass

    def update(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
