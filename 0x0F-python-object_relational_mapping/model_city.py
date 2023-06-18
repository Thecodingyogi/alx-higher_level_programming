#!/usr/bin/python3
"""Contains the class definition of a City."""
from model_state import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey


class City(Base):
    """Inherits from Base class"""
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
