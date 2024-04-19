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

    sql_query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        Where states.name = %s
        ORDER BY cities.id ASC
    """

    cur.execute(sql_query, (state_name,))

    query_rows = cur.fetchall()

    cities =[row[0] for row in query_rows]

    if cities:
        print(", ".join(cities))
    else:
        print("No cities found for the state:", state_name)

    cur.close()
    conn.close()


if __name__ == "__main__":
    user, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    list_cities_by_state(user, password, db_name, state_name)
