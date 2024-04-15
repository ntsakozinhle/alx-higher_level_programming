#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all cites whose match
argument
"""


import MySQLdb
import sys


def list_cities_by_state(user, password, db_name, state_name):
    """
    Connects to the specified MySQL database and lists all citiess whose name
    matches the argument
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()

    cur.execute("""
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        Where states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    user, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    list_cities_by_state(user, password, db_name, state_name)
