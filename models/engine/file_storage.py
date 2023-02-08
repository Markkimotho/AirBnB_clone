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
        """ serializes __objects to the JSON file (path: __file_path)
            Description:
        """

        store = {}
        for key in FileStorage.__objects.keys():
            store[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json_file.write(json.dumps(store))

    def reload(self):
        """ deserializes the JSON file to __objects
            if the JSON file (__file_path) exists ; otherwise, do nothing
        """
        try:
            with open(FileStorage.__file_path,
                      "r+", encoding="utf-8") as obj_file:
                FileStorage.__objects = {}
                temp = json.load(obj_file)
                for key in temp.keys():
                    cls = temp[key].pop("__class__", None)
                    cr_at = temp[key]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    up_at = temp[key]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[key] = eval(cls)(temp[key])
        except Exception as e:
            pass
