#!/usr/bin/python3
"""
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 5:
        import MySQLdb

        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        qry = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"
        c.execute(qry, (sys.argv[4],))
        res = c.fetchall()
        for i in res:
            print(row)

        c.close()
        if db:
            db.close()
