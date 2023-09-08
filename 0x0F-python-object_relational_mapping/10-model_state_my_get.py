#!/usr/bin/python3
"""
Prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) > 4:
        user = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]
        st = sys.argv[4]

        url = f"mysql+mysqlconnector://{user}:{pwd}@localhost:3306/{db}"
        engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()

        state = session.query(State).filter(
                State.name == st).order_by(State.id).first()

        if state:
            print(state.id)
        else:
            print("Not found")
        session.close()
