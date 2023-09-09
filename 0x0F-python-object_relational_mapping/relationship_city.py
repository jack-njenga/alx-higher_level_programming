#!/usr/bin/python3
"""
Improved City class with relationship
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import State, Base


class City(Base):
    """
    City class
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
