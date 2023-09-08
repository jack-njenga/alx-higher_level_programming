#!/usr/bin/python3
"""
Class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects import mysql

Base = declarative_base()


class State(Base):
    """
    State class
    """
    __tablename__ = "states"
    id = Column(mysql.INTEGER(11), primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
