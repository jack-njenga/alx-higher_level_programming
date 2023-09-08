#!/usr/bin/python3
"""
lists all cities of that state, using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    if len(sys.argv) == 5:
        import MySQLdb

        name = sys.argv[4]
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        qry = ("SELECT cities.name FROM states, cities WHERE "
               "cities.state_id = states.id AND states.name "
               "like '{}' ORDER BY cities.id").format(name)

        c.execute(qry)
        res = c.fetchall()
        lst = []
        for i in res:
            lst.append(i[0])
            # print(i[0], sep=", ", end="\n")
        print(*lst, sep=", ")

        c.close()
        db.close()
