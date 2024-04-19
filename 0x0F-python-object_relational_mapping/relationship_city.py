#!/usr/bin/python3
"""Defines the City class."""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """ City class representation.

    Args:
        Base (declarative_base()): Base class from SQLAlchemy.

    Attributes:
        __tablename__ (str): the name of the mySQL table
        id (sqlalchemy.Column): An auto-generated, unique integer ID
        name (sqlalchemy.Colum): A string representing the name
        state_id (sqlalchemy.Column): an integer representing th ID of state
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
