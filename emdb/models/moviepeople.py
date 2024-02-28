#!/usr/bin/python3
"""Sets up association class between movie and people."""
from .base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class MoviePeople(BaseModel, Base):
    """Representation of MoviePeople"""
    __tablename__ = 'tbl_movie_people'

    movie_id = Column(String(60), ForeignKey('tbl_movie.id'), nullable=False)
    people_id = Column(String(60), ForeignKey('tbl_people.id'), nullable=False)
    name = Column(String(250), nullable=True)

    # Defining relationship.
    rel_people = relationship("People", backref='movie')
    rel_movie = relationship("Movie", backref='people')

    def __init__(self):
        """Initialization of MoviePeople"""
        super().__init__()
