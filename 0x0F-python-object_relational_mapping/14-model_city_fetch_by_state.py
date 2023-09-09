#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    if len(sys.argv) == 4:
        user = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]

        url = f"mysql+mysqlconnector://{user}:{pwd}@localhost:3306/{db}"
        engine = create_engine(url, pool_pre_ping=True)
        # Base.metadata.create_all(engine)

        for key, val in Base.metadata.tables.items():
            print(key, "==>", val)
        print("====================================")
        session = sessionmaker(bind=engine)()

        cities = session.query(City, State.name).
        join(State).order_by(City.id).all()

        for city, stname in cities:
            print(f"{stname}: ({city.id}) {city.name}")

        session.close()
