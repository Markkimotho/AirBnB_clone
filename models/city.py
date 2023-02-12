#!/usr/bin/python3
""" A module with class City that inherits from BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """ class Review that manages all its instances """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an intance of City """
        super().__init__(*args, **kwargs)
