#!/usr/bin/python3
"""
safe from SQL injection
"""


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 4:
        import MySQLdb

        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], 
                passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        c.execute("SELECT * FROM cities ORDER BY id")

        results = c.fetchall()
        for i in results:
            print(i)
        
        c.close()
        if db:
            db.close()
