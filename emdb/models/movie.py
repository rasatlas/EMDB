#!/usr/bin/python3
"""Sets up class Movie."""
from base_model import Base, BaseModel
from sqlalchemy import Column, String, Date, Time, Double


class Movie(Base, BaseModel):
    """Representation of Movie"""
    __tablename__ = 'tbl_movie'

    title = Column(String(250), nullable=False)
    cover = Column(String(250), nullable=False)
    release_date = Column(Date, nullable=False)
    duration = Column(Time, nullable=False)
    synopsis = Column(String(2000), nullable=False)
    official_website = Column(String(250), nullable=True)
    budget = Column(Double, nullable=True)

    def __init__(self):
        """Initializing Movie"""
        super().__init__()
