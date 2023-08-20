#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""


def display_state(user, passwd, db_name, state_name):
    """
    displays states table with state_name provided as args
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

    query = "SELECT * FROM states WHERE name LIKE name = %s ORDER BY id"
    c.execute(query, (state_name,))
    states = c.fetchall()

    for state in states:
        print(state)

    if db:
        db.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]
        state = sys.argv[4]

        display_state(user, passwd, db_name, state)
