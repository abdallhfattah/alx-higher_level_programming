#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]  # state
    cur.execute(
        """SELECT cities.name FROM cities JOIN states ON state.id = cities.states_id 
        WHERE states.name LIKE %s""", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
