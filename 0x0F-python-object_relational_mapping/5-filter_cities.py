#!/usr/bin/python3
"""Get all states"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    query = "SELECT cities.name \
      From cities \
      INNER JOIN states ON states.id = cities.state_id \
      WHERE states.name = %s \
      ORDER BY cities.id ASC"
    cur.execute(query, (argv[4], ))
    req = cur.fetchall()
    s = []
    for r in req:
        s.append(" ".join(r))
    print(", ".join(s))
    cur.close()
    db.close()
