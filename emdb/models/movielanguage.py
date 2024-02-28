#!/usr/bin/python3
"""Sets up association class between movie and language."""
from .base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class MovieLanguage(BaseModel, Base):
    """Representation of MovieLanguage"""
    __tablename__ = 'tbl_movie_language'

    movie_id = Column(String(60), ForeignKey('tbl_movie.id'), nullable=False)
    language_id = Column(String(60), ForeignKey('tbl_language.id'),
                         nullable=False)

    # Define relationship
    movie = relationship("Movie", backref='language')
    language = relationship("Language", backref='movie')

    def __init__(self):
        """Initialization of MovieLanguage"""
        super().__init__()
