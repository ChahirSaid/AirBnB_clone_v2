#!/usr/bin/python3
"""Database storage Test"""
from models.engine.db_storage import DBStorage
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test is not relevant for DBStorage")
class test_DB_Storage(unittest.TestCase):
    """Database storage unittest"""

    def test_documentation(self):
        """documentation test"""
        self.assertIsNot(DBStorage.__doc__, None)
