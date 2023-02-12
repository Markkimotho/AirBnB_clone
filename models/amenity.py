#!/usr/bin/python3
""" A module with class Amenity that inherits from BaseModel """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class Amenity that manages all its instances """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an instance of amenity """
        super().__init__(*args, **kwargs)
