#!/usr/bin/python3

""" Module that for creating our CLI for the AirBnB Clone App"""
import cmd
import os


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quits the Terminal """
        sys.exit()

    def do_EOF(self, line):
        """ Defines the EOF:
        ->End of The Program
        ->Quits The Program/Terminal
        ---similar to quit()---
        """
        return True

    def do_create(self, line):
        pass
    def show(self, line):
        pass

    def destroy(self, line)
    def all(self, line)
    def update(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
