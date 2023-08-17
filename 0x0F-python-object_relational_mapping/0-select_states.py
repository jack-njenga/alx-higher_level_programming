#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""


def list_states(username, password, database):
    """
    lists all states from the database hbtn_0e_0_usa
    Note :
        if password stars with "#" escape it with "\"
        => so the correct way "\" instead
    """
    import MySQLdb as sqldb
    db_config = {
            "host": "localhost",
            "port": 3306,
            "user": username,
            "passwd": password,
            "db": database
            }
    try:
        db = sqldb.connect(**db_config)
        cursor = db.cursor()
    except sqldb.Error as e:
        print(e)
        sys.exit(1)

    query = "SELECT * FROM states ORDER BY states.id ASC"
    try:
        cursor.execute(query)
        states = cursor.fetchall()
    except sqldb.Error as e:
        print(e)
        db.close()
        sys.exit(1)

    for state in states:
        print(state)

    db.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_states(username, password, database)
