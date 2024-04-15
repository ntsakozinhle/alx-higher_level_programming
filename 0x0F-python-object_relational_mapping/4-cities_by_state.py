#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states whose match
argument
"""


import MySQLdb
import sys


def list_cities(user, password, db_name):
    """
    Connects to the specified MySQL database and lists all states whose name
    matches the argument
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()

    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    list_cities(user, password, db_name)
