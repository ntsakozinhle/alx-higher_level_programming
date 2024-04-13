#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    printed_states = set()

    for row in rows:
        state_id, state_name = row
        if state_name not in printed_states:
            printed_states.add(state_name)
            print(row)

    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
