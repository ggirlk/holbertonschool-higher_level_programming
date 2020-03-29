#!/usr/bin/python3
import sys
import MySQLdb


db=MySQLdb._mysql.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
db.query("SELECT * FROM states ORDER BY id ASC")
req=db.store_result()
for r in req.fetch_row(maxrows=0):
    print(r)
