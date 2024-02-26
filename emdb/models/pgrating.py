#!/usr/bin/python3
from .base_model import Base, BaseModel
from sqlalchemy import Column, String


class PgRating(Base, BaseModel):
    """Representation of Pg Rating."""
    __tablename__ = 'tbl_pg_rating'

    pg_rating = Column(String(250))

    def __init__(self):
        """Initializing PgRating."""
        super().__init__()
