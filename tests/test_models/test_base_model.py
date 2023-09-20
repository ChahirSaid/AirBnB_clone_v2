#!/usr/bin/python3
"""Test Base Model"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'Base model test not supported')
class test_basemodel(unittest.TestCase):
    """Test Base Model"""

    def __init__(self, *args, **kwargs):
        """Initialisation"""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Setup"""
        pass

    def tearDown(self):
        """TearDown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_default(self):
        """test default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """test kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """test kwargs int"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """test str"""
        i = self.value()
        self.assertEqual(str(i),
                         "[{}] ({}) {}".format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """todict test"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """kwargs none test"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """kwargs one test"""
        n = {"Name": "test"}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """id test"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """created at test """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """updated at test"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
