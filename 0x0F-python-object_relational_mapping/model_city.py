#!/usr/bin/python3
"""
City class
"""
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    This is city class
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
