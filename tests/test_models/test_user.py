#!/usr/bin/python3
"""User Test"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """test user"""

    def __init__(self, *args, **kwargs):
        """initialisation"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """first name test"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """last name test"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """email test"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """pwd test"""
        new = self.value()
        self.assertEqual(type(new.password), str)
