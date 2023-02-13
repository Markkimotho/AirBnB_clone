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
            print("** class name missing **")
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
        """ Prints the string representation of an instance
        based on the class name and id.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                # SEARCHING USING CLASS NAME & ID INSTANCE
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return
            else:
                # SEARCHING AND DELETING USING ID INSTANCE
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
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
                print("** class doesn't exist **")
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
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif (args[0]+"."+args[1]) not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
            elif len(args) == 4:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                    return
                else:
                    setattr(storage.all()[key], args[2], args[3].strip('\"'))
                    storage.save()
                    return

    # <class name>.action()

    def do_User(self, arg):
        """Mode Of Operation:
        User.all() - displays all objects of class User
        User.count() - displays number of objects of class User
        User.show(<id>) - displays object of class User with id
        User.destroy(<id>) - deletes object of class User with id
        User.update(<id>, <attribute name>, <attribute value>) - update User
        User.update(<id>, <dictionary representation>) - update User
        """
        self.class_helper('User', arg)

    def do_BaseModel(self, arg):
        """Mode Of Operation:
        BaseModel.all() - displays all objects of class BaseModel
        BaseModel.count() - displays number of objects of class BaseModel
        BaseModel.show(<id>) - displays object of class BaseModel with id
        BaseModel.destroy(<id>) - deletes object of class BaseModel with id
        BaseModel.update(<id>, <attribute name>, <attribute value>) - update
        BaseModel.update(<id>, <dictionary representation>) - update
        """
        self.class_helper('BaseModel', arg)

    def do_State(self, arg):
        """Mode Of Operation:
        State.all() - displays all objects of class State
        State.count() - displays number of objects of class State
        State.show(<id>) - displays object of class State with id
        State.destroy(<id>) - deletes object of class BaseModel with id
        State.update(<id>, <attribute name>, <attribute value>) - update
        State.update(<id>, <dictionary representation>) - update
        """
        self.class_helper('State', arg)

    def do_City(self, arg):
        """Mode Of Operation:
        City.all() - displays all objects of class City
        City.count() - displays number of objects of class City
        City.show(<id>) - displays object of class City with id
        City.destroy(<id>) - deletes object of class City with id
        City.update(<id>, <attribute name>, <attribute value>) - update
        City.update(<id>, <dictionary representation>) - update
        """
        self.class_helper('City', arg)

    def do_Amenity(self, arg):
        """Mode Of Operation:
        Amenity.all() - displays all objects of class Amenity
        Amenity.count() - displays number of objects of class Amenity
        Amenity.show(<id>) - displays object of class Amenity with id
        Amenity.destroy(<id>) - deletes object of class Amenity with id
        Amenity.update(<id>, <attribute name>, <attribute value>) - update
        Amenity.update(<id>, <dictionary representation>) - update
        """
        self.class_helper('Amenity', arg)

    def do_Place(self, arg):
        """Mode Of Operation:
        Place.all() - displays all objects of class Place
        Place.count() - displays number of objects of class Place
        Place.show(<id>) - displays object of class Place with id
        Place.destroy(<id>) - deletes object of class Place with id
        Place.update(<id>, <attribute name>, <attribute value>) - update
        Place.update(<id>, <dictionary representation>) - update
        """
        self.class_helper('Place', arg)

    def do_Review(self, arg):
        """Mode Of Operation:
        Review.all() - displays all objects of class Review
        Review.count() - displays number of objects of class Review
        Review.show(<id>) - displays object of class Review with id
        Review.destroy(<id>) - deletes object of class Review with id
        Review.update(<id>, <attribute name>, <attribute value>) - update
        Review.update(<id>, <dictionary representation>) - update
        """
        self.class_helper('Review', arg)

    def class_helper(self, class_name, arg):
        """ helper function for the section <class name>.action """

        if arg == '.all()':
            self.do_all(class_name)
        elif arg == '.count()':
            count = 0
            for key in storage.all().keys():
                count += 1
            print(count)
        elif arg[:6] == '.show(':
            self.do_show(class_name + ' ' + arg[7:-2])
        elif arg[:9] == '.destroy(':
            self.do_destroy(class_name + ' ' + arg[10:-2])
        elif arg[:8] == '.update(':
            if '{' in arg and '}' in arg:
                new_arg = arg[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = arg[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(class_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dict = eval(new_arg[1])
                except Exception:
                    return
                for j in dict.keys():
                    self.do_update(class_name + ' ' +
                                   new_arg[0][1:-3]
                                   + ' ' + str(j) +
                                   ' ' + str(dict[j]))
            else:
                return
        else:
            print("Not a valid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
