#!/usr/bin/python3
""" A module with class Review that inherits from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review that manages all its instances """

    place_id = ""
    user_id = ""
    text = ""
