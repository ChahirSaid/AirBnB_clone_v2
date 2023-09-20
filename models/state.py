#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    if models.storage_t == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """Method that gets cities"""
            cityList = []
            for cityV in models.storage.all(City).values():
                if getattr(cityV, "state_id") == self.id:
                    cityList.append(cityV)
            return cityList
