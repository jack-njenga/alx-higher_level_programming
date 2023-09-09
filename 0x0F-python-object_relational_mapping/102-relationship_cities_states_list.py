#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State, Base

    if len(sys.argv) == 4:
        user = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]

        url = f"mysql+mysqlconnector://{user}:{pwd}@localhost:3306/{db}"
        engine = create_engine(url, pool_pre_ping=True)
        session = sessionmaker(bind=engine)()

        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            state = city.state.name
            print(f"{city.id}: {city.name} -> {state}")

        if session:
            session.close()
