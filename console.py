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
            return
        elif arg not in storage.classes(): 
            print("** class doesn't exist **")
            return
        else:
            classes_dict = storage.classes()
            obj = storage.all()
            print(obj)
            print(classes_dict)
            class_str = classes_dict[arg]()
            print(class_str)
            class_str.save()
            print(type(class_str))
            print(class_str.id)
            return

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id. """
        if arg == "" or arg is None:
            print("** class name is missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print(" ** instance id missing ** ")
                return
            else:
                
                #ADD SOME CODE HERE TO SEARCH USING ID INSTANCE
                
                print(" ** no instance found ** ")
                
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id 
        (save the change into the JSON file)
        """
        if arg == "" or arg is None:
            print(" ** class name missing ** ")
            return
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print(" **class name doesn't exist** ")
                return
            if len(args) == 1:
                print(" ** instance id missing ** ")
                return
            else:

                #ADD SOME CODE HERE TO SEARCH USING ID INSTANCE
                
                print(" ** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        """

        if arg or arg == "" or arg is None:

            # THE STRING REPRESENTATION OF INSTANCES.

            print(arg)
        if arg not in storage.classes():
            print(" ** class doesn't exist ** ")
            return

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
