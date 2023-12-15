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
    cur.execute("SELECT cities.name \
    FROM cities JOIN states ON cities.states_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))
    result = cur.fetchall()
    print(", ".join([lis[0] for lis in result]))
