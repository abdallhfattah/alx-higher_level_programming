#!/usr/bin/python3
"""  list target state from the database hbtn_0e_0_usa """
import sys

import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id , cities.name , state.name FROM cities , state where state.id = cities.state_id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
