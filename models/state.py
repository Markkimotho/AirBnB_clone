#!/usr/bin/python3
""" A module with class State that inherits from BaseModel """

from models.base_model import BaseModel


class State(BaseModel):
    """ class State that manages all its instances """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an instance of State """
        super().__init__(*args, **kwargs)
