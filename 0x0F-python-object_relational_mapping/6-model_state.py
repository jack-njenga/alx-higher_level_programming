#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    url = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@\
            localhost/{sys.argv[3]}"
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
