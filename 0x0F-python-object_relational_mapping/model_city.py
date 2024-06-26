#!/usr/bin/python3
"""
Contains City class and Base, an instance of declarative_base()
"""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
   Class with id and name attributes of each City
   """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,  ForeignKey("states.id"), nullable=False)
