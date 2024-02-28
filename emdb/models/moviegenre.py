#!/usr/bin/python3
"""Sets up association class between movie and genre."""
from .base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class MovieGenre(BaseModel, Base):
    """Representation of MovieGenre"""
    __tablename__ = 'tbl_movie_genre'

    movie_id = Column(String(60), ForeignKey('tbl_movie.id'), nullable=False)
    genre_id = Column(String(60), ForeignKey('tbl_genre.id'), nullable=False)

    # Define relationship
    rel_movie = relationship("Movie", backref='genre')
    rel_genre = relationship("Genre", backref='movie')

    def __init__(self):
        """Initialization of MoviePeople"""
        super().__init__()
