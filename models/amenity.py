#!/usr/bin/python3
""" amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Rep """
    name = ""

    def __init__(self, *args, **kwargs):
        """ init Amenity """
        super().__init__(*args, **kwargs)