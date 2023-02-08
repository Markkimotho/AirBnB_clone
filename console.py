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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
