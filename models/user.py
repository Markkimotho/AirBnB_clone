#!/usr/bin/python3

""" module containing class User that inherits from BaseModel """
from models.base_model import BaseModel
from models import storage
class User(BaseModel):
    """User class that defines a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
