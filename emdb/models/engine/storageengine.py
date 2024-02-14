#!/usr/bin/python3
"""This module defines the StorageEngine class that implements database
    related activities.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import configparser


class StorageEngine:
    """Class that handles activities pertaining the MySQL database."""
    __engine = None
    __session = None
    __congif = None

    def __init__(self):
        """Instantiate a StorageEngine object."""
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
        pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass

    def close(self):
        pass

    def get(self, cls, id):
        pass
