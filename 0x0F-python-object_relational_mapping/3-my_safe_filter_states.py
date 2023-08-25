#!/usr/bin/python3
"""
sql injection
"""


def state_search(user, passwd, db_name, name):
    """
    searches for state with $name
    """
    import MySQLdb

    db_config = {
            "host": "localhost",
            "port": 3306,
            "user": user,
            "passwd": passwd,
            "db": db_name
            }
    db = MySQLdb.connect(**db_config)
    c = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name='{}' ORDER\
             BY id ASC".format(name)
    c.execute(query)

    states = c.fetchall()
    for state in states:
        print(state)

    if db:
        db.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]

        state_search(user, passwd, db, sys.argv[4])
