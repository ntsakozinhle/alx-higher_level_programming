#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states whose names
start with 'N' in ascending order by their ID.
"""

import MySQLdb
import sys

def filter_states(user, password, db_name):
   """
   Connects to the specified MySQL database and lists all states whose names
   with 'N'
   """
   conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name, charset="utf8")
   cur = conn.cursor()

   cur.execute("SELECT * FROM states WHERE name LIKE 'N%'  ORDER BY id ASC")

   query_rows = cur.fetchall()

   for row in query_rows:
       print(row)

   cur.close()
   conn.close()

if __name__ == "__main__":
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states(user, password, db_name)
