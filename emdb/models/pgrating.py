#!/usr/bin/python3
from .base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class PgRating(BaseModel, Base):
    """Representation of Pg Rating."""
    __tablename__ = 'tbl_pg_rating'

    pg_rating = Column(String(250))
    movies = relationship("MoviePgRating", backref='pgrating')

    def __init__(self):
        """Initializing PgRating."""
        super().__init__()
