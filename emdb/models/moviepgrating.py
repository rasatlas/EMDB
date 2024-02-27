#!/usr/bin/python3
"""Sets up association class between movie and pgrating."""
from .base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class MoviePgRating(BaseModel, Base):
    """Representation of MoviePgRating"""
    __tablename__ = 'tbl_movie_pg_rating'

    movie_id = Column(String(60), ForeignKey('tbl_movie.id'), nullable=False)
    pg_rating_id = Column(String(60), ForeignKey('tbl_pg_rating.id'),
                          nullable=False)
    content = Column(String(250), nullable=True)

    def __init__(self):
        """Initialization of MoviePgRating"""
        super().__init__()
