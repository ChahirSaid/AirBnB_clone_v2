#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.place import place_amenity
import models


class Amenity(BaseModel, Base):
    """class Amenity"""

    __tablename__ = "amenities"

    if models.storage_t == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""
