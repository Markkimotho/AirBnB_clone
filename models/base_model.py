#!/usr/bin/python3

from datetime import datetime
import uuid

""" A module that defines the "BaseModel" class """


class BaseModel:
    """base class called BaseModel:
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes an object of class BaseModel
        """
        if len(kwargs) > 0:
            pass
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()



    def __str__(self):
        """Returns string representation of an object
        """
        return "{[]} {()} {}"\
                .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        pass
