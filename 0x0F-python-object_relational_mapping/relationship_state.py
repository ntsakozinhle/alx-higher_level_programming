#!/usr/bin/python3
"""
Defines the State class.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """
    State class representation.

    Args:
        Base (declarative_base()): Base class from SQLAlchemy.

    Attributes:
        __tablename__ (str): the name of the mySQL table
        id (sqlalchemy.Column): An auto-generated, unique integer ID
        name (sqlalchemy.Colum): A string representing the name
        cities (sqlalchemy.Column): Relationship to the City Object
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete")
