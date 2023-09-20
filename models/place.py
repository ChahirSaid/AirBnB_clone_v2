#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models

if models.storage_t == "db":
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
        ),
    )
else:
    place_amenity = {}


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    if models.storage_t == "db":
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities",
            viewonly=False,
        )
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns list of review instances with place_id
            equals to the cyrrent Place.id
            FileStorage relationship between Place and Review
            """
            from models import storage

            all_revs = storage.all(Review)
            list_revs = []
            for rev in all_revs.values():
                if rev.place_id == self.id:
                    list_revs.append(rev)
            return list_revs

        @property
        def amenities(self):
            """amenities"""
            from models import storage
            from models.amenity import Amenity

            all_amens = storage.all(Amenity)
            list_amen = []
            for amen in all_amens.values():
                if amen.id in self.amenity_ids:
                    list_amen.append(amen)
            return list_amen

        @amenities.setter
        def amenities(self, obj):
            """
            amenities
            """
            from models.amenity import Amenity

            if obj:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
