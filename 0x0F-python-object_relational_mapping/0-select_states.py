#!/usr/bin/python3
""" select states"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    # connect to database
    username, password, database = argv[1:4]
    db = MySQLdb.connect(user=username, passwd=password, db=database)

    # set a cursor
    c = db.cursor()

    # sql querie
    c.execute("""SELECT * FROM states;""")
    states = c.fetchall()

    # print results
    for i in states:
        print(i)
