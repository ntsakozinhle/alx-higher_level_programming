#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states whose match
argument
"""


import MySQLdb
import sys

def filter_states(user, password, db_name, state_name):
    """
    Connects to the specified MySQL database and lists all states whose name
    matches the argument
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()

    sql_query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC LIMIT 1".format(state_name)

    cur.execute(sql_query)

    query_rows = cur.fetchall()

    if query_rows:
        for row in query_rows:
            print(row)

    else:
        print("No records found for the state:", state_name)

    cur.close()
    conn.close()


if __name__ == "__main__":
    user, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    filter_states(user, password, db_name, state_name)
