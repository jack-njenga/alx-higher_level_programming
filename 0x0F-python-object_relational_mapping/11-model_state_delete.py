#!/usr/bin/python3
"""
Delets a State instance
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    url = "mysql+mysqlconnector://root:#Jarvis9101@\
           localhost:3306/hbtn_0e_6_usa"
    engine = create_engine(url, pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    kwargs = {}
    args = sys.argv
    for arg in args:
        if "=" in arg:
            key = arg.split("=")[0]
            val = arg.split("=")[1]
            kwargs[key] = val

    sts = session.query(State).filter_by(**kwargs).all()

    for st in sts:
        print(st.id)
        session.delete(st)
        session.commit()
        print(st, "Succesfully Deleted")
