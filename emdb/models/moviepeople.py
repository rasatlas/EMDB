#!/usr/bin/python3
"""Sets up association class between movie and people."""
from .base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class MoviePeople(Base, BaseModel):
    """Representation of MoviePeople"""
    __tablename__ = 'tbl_movie_people'

    movie_id = Column(String(60), ForeignKey('tbl_movie.id'), nullable=False)
    people_id = Column(String(60), ForeignKey('tbl_people.id'), nullable=False)
    name = Column(String(250), nullable=False)

    def __init__(self):
        """Initialization of MoviePeople"""
        super().__init__()
