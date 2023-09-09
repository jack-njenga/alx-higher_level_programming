#!/usr/bin/python3
"""
Creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
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
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()

        new_state = State(name="Clifornia")
        session.add(new_state)

        new_city = City(name="San Francisco", state=new_state)
        session.add(new_city)

        session.commit()

        if session:
            session.close()
