#!/usr/bin/python3
"""
Lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import Base, State

    if len(sys.argv) == 4:
        user = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]

        url = f"mysql+mysqlconnector://{user}:{pwd}@localhost:3306/{db}"
        engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()

        states = session.query(State).order_by(State.id).all()

        for state in states:
            print(f"{state.id}: {state.name}")
            for city in sorted(state.cities, key=lambda c: c.id):
                print(f"\t{city.id}: {city.name}")

        if session:
            session.close()
