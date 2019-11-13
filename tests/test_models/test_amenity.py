#!/usr/bin/python3
""" Unittesting for BaseModel """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import uuid
from models.base_model import BaseModel
import pep8

class test_amenity(unittest.TestCase):
    """ test class """
    def test_pep8(self):
        """ test pep8 """

        pep8check = pep8.StyleGuide(quiet=True)
        check = pep8check.check_files(["models/base_model.py"])
        self.assertEqual(check.total_errors, 0,
                "Found code errors")