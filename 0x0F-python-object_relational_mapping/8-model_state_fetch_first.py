#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(argv) > 3:
        user = argv[1]
        pwd = argv[2]
        db = argv[3]
        
        url = f"mysql+mysqlconnector://{user}:{pwd}@localhost:3306/{db}"
        engine = create_engine(url)
        session = sessionmaker(bind=engine)()

        state = session.query(State).order_by(State.id).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
        session.close()
