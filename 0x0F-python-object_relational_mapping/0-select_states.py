#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states in ascending
order by their ID
"""


import MySQLdb
import sys


def list_states(user, password, db_name):
    """
    Lists all unique states from the 'states table in the specified database
    """

    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name, charset='utf8')
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states(user, password, db_name)
