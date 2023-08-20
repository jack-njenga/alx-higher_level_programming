#!/usr/bin/python3
"""
Family script for family_db database
"""


def query_db(name, passwd, db):
    """
    """
    import MySQLdb as sqldb
    try:
        db = sqldb.connect(host="localhost", port=3306, user=name, passwd=passwd, db=db)
        cursor = db.cursor()
    except sqldb.Error as e:
        print("SQL ERROR :", e)
        sys.exit(1)

    query = "SELECT * FROM family_members ORDER BY family_members.id"

    try:
        cursor.execute(query)
        members = cursor.fetchall()
    except sqldb.Error as e:
        print("SQL ERROR :", e)
        db.close()
        sys.exit(1)

    for member in members:
        print(member)

    db.close()


if __name__ == "__main__":
    import sys

    args =  sys.argv
    if len(args) > 1:
        if len(args) > 2:
            if len(args) > 3:
                username = args[1]
                password = args[2]
                database = args[3]

                query_db(username, password, database)
            else:
                print("== Please Provide a Database ==")
        else:
            print("== Please Provide a Password ==")
    else:
        print("=== Please Provide Username ===")
