#!/usr/bin/python3
"""
state class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects import mysql
Base = declarative_base()


class State(Base):
    """
    States
    """
    __tablename__ = "states"
    id = Column(mysql.INTEGER(11), primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
