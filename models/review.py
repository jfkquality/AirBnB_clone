#!/usr/bin/python3
""" review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ review rep """
    place_id = ""
    user_id = ""
    text = ""

    def __init(self, *args, **kwargs):
        """ init review """
        super().__init__(*args, **kwargs)