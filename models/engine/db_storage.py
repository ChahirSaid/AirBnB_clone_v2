#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv

classes = {
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class DBStorage:
    """DataBase class Storage"""

    __engine = None
    __session = None

    def __init__(self):
        """init"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all"""
        objs = {}
        if cls:
            for name in classes:
                if cls == name:
                    find = self.__session.query(classes[name]).all()
                    for i in find:
                        key = i.__class__.__name__ + "." + i.id
                        objs[key] = i
        else:
            for name in classes:
                find = self.__session.query(classes[name]).all()
                for i in find:
                    key = i.__class__.__name__ + "." + i.id
                    objs[key] = i
        return objs

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self, remove=False):
        """reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        if remove:
            Session.remove()
        self.__session = Session
