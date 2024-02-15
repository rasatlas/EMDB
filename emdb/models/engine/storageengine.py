#!/usr/bin/python3
""" This module defines the StorageEngine class that implements database
    related activities.
"""

import models
from models.base_model import Base
from models.genre import Genre
from models.language import Language
from models.movie import Movie
from models.moviegenre import MovieGenre
from models.movielanguage import MovieLanguage
from models.moviepeople import MoviePeople
from models.moviepgrating import MoviePgRating
from models.people import People
from models.pgrating import PgRating
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import configparser


classes = {"Genre": Genre, "language": Language, "Movie": Movie,
           "MovieGenre": MovieGenre, "MovieLanguage": MovieLanguage,
           "MoviePeople": MoviePeople, "MoviePgRating": MoviePgRating,
           "People": People, "PgRating": PgRating}


class StorageEngine:
    """ Class that handles activities pertaining the MySQL database."""
    __engine = None
    __session = None
    __config = None

    def __init__(self):
        """ Instantiate a StorageEngine object."""
        self.__config = self.__read_config()
        EMDB_MYSQL_HOST = self.__config.get('database', 'host')
        EMDB_MYSQL_DB = self.__config.get('database', 'database')
        EMDB_MYSQL_USER = self.__config.get('database', 'user')
        EMDB_MYSQL_PWD = self.__config.get('database', 'password')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(EMDB_MYSQL_USER, EMDB_MYSQL_PWD,
                                             EMDB_MYSQL_HOST, EMDB_MYSQL_DB,
                                             pool_pre_ping=True))

    def __read_config(self, file_path='config.ini'):
        config = configparser.ConfigParser()
        config.read(file_path)
        return config

    def all(self, cls=None):
        """Query on the current database session."""
        dict = {}
        for c in classes:
            if cls is None or cls is classes[c] or cls is c:
                objs = self.__session.query(classes[c]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict[key] = obj
        return (dict)

    def new(self, obj):
        """ Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session if obj is not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads all data from the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """ Call remove() method on the private session attribute
            to remove open session.
        """
        self.__session.remove()

    def get(self, cls, id):
        """ A method to retrieve on object.
            Returns the object based on the class name and its id, or
            None if not found.
        """
        if cls not in classes.values():
            return None
        else:
            all_classes = models.storage.all()
            for val in all_classes.values():
                if (val.id == id):
                    return val