#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""


def list_states(username, password, database):
    """
    lists all states from the database hbtn_0e_0_usa
    Note :
        if password stars with "#" escape it with "\"
        => so the correct way "\" followed by "#" instead
    """
    import MySQLdb as sqldb
    db_config = {
            "host": "localhost",
            "port": 3306,
            "user": username,
            "passwd": password,
            "db": database
            }
    db = sqldb.connect(**db_config)
    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY states.id ASC"

    cursor.execute(query)
    states = cursor.fetchall()

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
