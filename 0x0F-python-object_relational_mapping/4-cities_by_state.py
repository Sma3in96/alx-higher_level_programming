#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa starts with "N"
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.states_id = states.id;")
    result = cur.fetchall()

    for i in result:
        print(i)
