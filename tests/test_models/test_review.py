#!/usr/bin/python3
"""Review Test"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """test review"""

    def __init__(self, *args, **kwargs):
        """initialisation"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """placeid test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """uid test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """text test"""
        new = self.value()
        self.assertEqual(type(new.text), str)
