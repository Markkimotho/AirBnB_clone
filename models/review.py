#!/usr/bin/python3
""" A module with class Review that inherits from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review that manages all its instances """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an instance of Review """
        super().__init__(*args, **kwargs)
