#!/usr/bin/python3
"""  list target state from the database hbtn_0e_0_usa & safe from sql injections """
import sys

import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    state = sys.argv[4]
    if (state.find('--') or state.find('TRUNCATE') or state.find('DROP') or state.find('ALTER')):
        sys.exit()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(state))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
