#!/usr/bin/python3
"""Unittest for Db storage"""

from models.engine.db_storage import DBStorage
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test is not relevant for DBStorage"
)
class test_DB_Storage(unittest.TestCase):
    """test dbstorage"""

    def test_documentation(self):
        """test doc"""
        self.assertIsNot(DBStorage.__doc__, None)