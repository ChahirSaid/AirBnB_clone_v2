#!/usr/bin/python3
"""Place Test"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """test place"""

    def __init__(self, *args, **kwargs):
        """initialisation"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """city test"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """uid test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """name test"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """desc test"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """number of rooms test"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """number of bathrooms test"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """max guest test"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """price per night test"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """latitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """long latitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """amenity id test"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
