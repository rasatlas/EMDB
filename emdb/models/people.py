#!/usr/bin/python3
"""Sets up class People."""
from .base_model import Base, BaseModel
from sqlalchemy import Column, String, Date, Integer


class People(Base, BaseModel):
    """Representation of People"""
    __tablename__ = 'tbl_people'

    first_name = Column(String(250), nullable=False)
    father_name = Column(String(250), nullable=False)
    grand_father_name = Column(String(250), nullable=True)
    birth_date = Column(Date, nullable=True)
    death_date = Column(Date, nullable=True)
    height = Column(Integer, nullable=True)
    head_shot = Column(String(250), nullable=False)

    def __init__(self):
        """Initializing People"""
        super().__init__()
