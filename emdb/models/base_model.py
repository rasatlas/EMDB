#!/usr/bin/python3
"""Sets up class BaseModel."""

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)

    def __init__(self):
        """Initializing the BaseModel"""
        self.id = str(uuid4())

    def save(self):
        pass

    def delete(self):
        pass

    def __str__(self):
        """String representation of the BaseModel."""
        return f"[{self.__class__.__name__}] <{self.id}>"
