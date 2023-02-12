#!/usr/bin/python3
""" A module with class User that inherits from BaseModel """

from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """User class that defines a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an instance of User """
        super().__init__(*args, **kwargs)
