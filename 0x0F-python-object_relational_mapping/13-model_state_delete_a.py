#!/usr/bin/python3
"""
Deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) == 4:
        user = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]

        url = f"mysql+mysqlconnector://{user}:{pwd}@localhost:3306/{db}"
        engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        sts = session.query(State).filter(State.name.like("%a%")).all()

        for st in sts:
            print(f"Deleting {st.name}...")
            session.delete(st)

        session.commit()
        session.close()
