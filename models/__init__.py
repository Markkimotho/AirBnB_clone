#!/usr/bin/python3
""" It Initializes the Package """

from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
