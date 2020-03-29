#!/usr/bin/python3
"""Get all states"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
      From cities \
      INNER JOIN states ON states.id = cities.state_id \
      ORDER BY id ASC"
    cur.execute(query)
    req = cur.fetchall()
    for r in req:
        """print("({}, '{}')".format(r[0], r[1]))"""
        print(r)
    cur.close()
    db.close()
