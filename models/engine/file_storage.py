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
    
    def classes(self):
        """Returns a dictionary of valid classes
        along with their references
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes_dict = {"BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Place": Place,
                        "Review": Review}

        return classes_dict

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """

        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
            Description:
                converting a Python object(dictionary)
                into a JSON-formatted string and writing it to a file.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            dict_obj = {key: value.to_dict()
                  for key, value in FileStorage.__objects.items()}
            json.dump(dict_obj, json_file)

    def reload(self):
        """ deserializes the JSON file to __objects
            if the JSON file (__file_path) exists ; otherwise, do nothing
            Description:
                Reading a JSON-formatted data from a file
                and converting it to a python dictionary(object)
        """
        file_exists = exists(FileStorage.__file_path)
        if file_exists:
            with open(FileStorage.__file_path, "r+", encoding="utf-8") as json_file:
                dict_obj = json.load(json_file)
#               print(dict_obj) #For Testing
                dict_obj = {key: self.classes()[value["__class__"]](**value)
                       for key, value in dict_obj.items()}
#               print(dict_obj) #For Testing
        else:
            return
