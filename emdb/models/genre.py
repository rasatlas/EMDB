#!/usr/bin/python3
"""Sets up class Genre"""
from .base_model import Base, BaseModel
from sqlalchemy import Column, String


class Genre(Base, BaseModel):
    """Representation of Genre"""
    __tablename__ = 'tbl_genre'

    genre = Column(String(250), unique=True, nullable=False)

    def __init__(self):
        """Initializing Genre"""
        super().__init__()
