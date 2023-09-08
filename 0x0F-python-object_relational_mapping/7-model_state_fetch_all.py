#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import State
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker

    if len(argv) > 3:
        user = argv[1]
        pwd = argv[2]
        db = argv[3]

        engine = sqlalchemy.create_engine(
                "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                    user, pwd, db), pool_pre_ping=True)

        session = sessionmaker(bind=engine)()
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(state.id, ":", state.name)
        session.close()
