#!/usr/bin/python3

""" A module with the 'FileStorage' class """
import json
from os.path import exists


class FileStorage:
    """ class FileStorage that:
    ->serializes instances to a JSON file and
    ->deserializes JSON file to instances
    """
    __file_path = "file.path"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """

        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as json_file:
            objects = {key: value.to_dict()
                       for key, value in FileStorage.__objects.items()}
            json.dump(objects, json_file)

    def reload(self):
        """ deserializes the JSON file to __objects
            if the JSON file (__file_path) exists ; otherwise, do nothing
        """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8")as obj_file:
                obj_dict = json.load(obj_file)
                obj_dict = {key: self.classes()[value["__class__"]](**value)
                            for key, value in obj_dict.items()}
                FileStorage.__objects = obj_dict
