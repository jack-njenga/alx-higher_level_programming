#!/usr/bin/python3
"""
lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
"""


def list_n_states(username, passwd, d_b):
    import MySQLdb as sqldb
    """
    lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa.
    """
    try:
        db_config = {
                "host": "localhost",
                "port": 3306,
                "user": username,
                "passwd": passwd,
                "db": d_b
                }
        db = sqldb.connect(**db_config)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
        cursor.execute(query)

        states = cursor.fetchall()
        for state in states:
            print(state)

    except sqldb.Error as e:
        print(e)
    if db:
        db.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 4:
        name = sys.argv[1]
        passwd = sys.argv[2]
        d_b = sys.argv[3]
        list_n_states(name, passwd, d_b)
