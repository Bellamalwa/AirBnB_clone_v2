#!/usr/bin/python3
"""Test console"""

import os
import uuid
import unittest
import models
from io import StringIO
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
	"""Unittesting the HBNB Command interpreter"""
@classmethod
    def setUpClass(test_cls):
        try:
            os.rename("file.json", "tmp_file")
        except IOError:
            pass
        test_cls.HBNB = HBNBCommand()

@classmethod
    def tearDownClass(test_cls):
        try:
            os.rename("tmp_file", "file.json")
        except IOError:
            pass
        del test_cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

def setUp(self):
        FileStorage._FileStorage__objects = {}

def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

@unittest.skipIf(type(models.storage) == DBStorage, "Testing DBstorage")
    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create BaseMOdel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Amenity")
            new_amenity = test.getvalue().strip()
if __name__ = '__main__':
	unittest.main()