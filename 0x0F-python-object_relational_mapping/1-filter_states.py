#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa statring with N"""
import sys

import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        id , state = row.split(',')
        if(state.startswith(' (N')):
            print(row)
    cur.close()
    conn.close()
