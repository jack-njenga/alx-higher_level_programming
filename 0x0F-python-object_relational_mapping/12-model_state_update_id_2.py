#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
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

        st = session.query(State).filter_by(id=2).first()

        if st:
            # print("Updating")
            st.name = "New Mexico"
            session.commit()
        session.close()
