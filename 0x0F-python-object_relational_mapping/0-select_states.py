#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys

import MySQLdb

print(sys.argv)
if __name__ == "__main__":
    conn = MySQLdb.connect(
        username=sys.argv[1], password=sys.argv[2], database=sys.argv[3], host="localhost", port=3306)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()