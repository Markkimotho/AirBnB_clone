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
            class_str = classes_dict[arg]()
            class_str.save()
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
                #SEARCHING USING CLASS NAME & ID INSTANCE
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print(" ** no instance found ** ")
                else:
                    print(storage.all()[key])

                    

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
                #SEARCHING AND DELETING USING ID INSTANCE
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print(" ** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        # THE STRING REPRESENTATION OF ALL INSTANCES.
        if arg == "":
            all_list = [(str(value))
                        for key, value in storage.all().items()]
            print(all_list)
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print(" ** class doesn't exist ** ")
                return
            else:
                class_list = [str(value)
                              for key, value in storage.all().items()
                              if type(value).__name__ == args[0]]
                print(class_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return
        else:
            args = arg.split(" ")
            if args[0] not in storage.classes():
                print("** class name doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")

            key = f"{args[0]}.{args[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
                return
            else:
                for key in storage.all():
                    print(storage.all()[key])
                    print()
                    print(storage.all()[key].to_dict())
                    print()
                    for k, v in storage.all()[key].to_dict().items():
                        print(k,":",v)
                    print()
                    storage.all()[key].to_dict()["name"] = "Mark"
                    storage.save
                    for i, j in storage.all()[key].to_dict().items():
                        print(i,":",j)
                        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
