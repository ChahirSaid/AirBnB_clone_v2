#!/usr/bin/python3
"""A unit test module for the console"""
import unittest
import console


class test_Console(unittest.TestCase):
    """Represents the test class for the HBNBCommand class"""

    def test_documentation(self):
        """test documentation"""
        self.assertIsNotNone(console.__doc__)
