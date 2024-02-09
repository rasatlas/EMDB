#!/usr/bin/python3
"""Sets up class Language"""
from base_model import Base, BaseModel
from sqlalchemy import Column, String


class Language(Base, BaseModel):
    """Representation of Language"""
    __tablename__ = "tbl_language"

    language = Column(String(250), unique=True, nullable=False)

    def __init__(self):
        """Initializing Language"""
        super().__init__()
