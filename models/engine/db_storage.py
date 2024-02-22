#!/usr/bin/python3
"""
SQL script documentation explaining the purpose of db_storage.py.
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """
    Class documentation explaining the purpose of DBStorage.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Method documentation explaining the purpose of __init__ method.
        """

    def all(self, cls=None):
        """
        Method documentation explaining the purpose of the all method.
        """

    def new(self, obj):
        """
        Method documentation explaining the purpose of the new method.
        """

    def save(self):
        """
        Method documentation explaining the purpose of the save method.
        """

    def delete(self, obj=None):
        """
        Method documentation explaining the purpose of the delete method.
        """

    def reload(self):
        """
        Method documentation explaining the purpose of the reload method.
        """
