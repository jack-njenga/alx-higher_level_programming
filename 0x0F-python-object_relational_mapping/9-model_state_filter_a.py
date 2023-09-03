#!/usr/bin/python3
"""
lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    if len(argv) > 3:
        user = argv[1]
        pwd = argv[2]
        db = argv[3]

        url = f"mysql+mysqlconnector://{user}:{pwd}@localhost:3306/{db}"
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()

        states = session.query(State).filter(
                State.name.like("%a%")).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")

        session.close()
