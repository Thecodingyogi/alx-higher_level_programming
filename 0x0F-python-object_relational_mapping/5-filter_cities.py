#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all cities
    of that state using the database.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
            """
            SELECT * FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id""")
    print(", ".join([city[2]
                     for city in cur.fetchall()
                     if city[4] == sys.argv[4]]))
    cur.close()
    db.close()
