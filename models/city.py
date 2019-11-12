#!/usr/bin/python3
""" class city """
from models.base_model import BaseModel


class City(BaseModel):
    """ city rep """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ init city """
        super().__init__(*args, **kwargs)