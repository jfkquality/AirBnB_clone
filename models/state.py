#!/usr/bin/python3
""" class State """
from models.base_model import BaseModel


class State(BaseModel):
    """ state rep """
    name = ""

    def __init__(self, *args, **kwargs):
        """ init state """
        super().__init__(*args, **kwargs)