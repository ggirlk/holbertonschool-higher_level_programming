#!/usr/bin/python3
"""Get all states"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (argv[4], ))
    req = cur.fetchall()
    for r in req:
        print("({}, '{}')".format(r[0], r[1]))
    cur.close()
    db.close()
