#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    unique_states = set()

    results = cursor.fetchall()

    for row in results:
        state_id, state_name = row
        if state_name not in unique_states:
            unique_states.add(state_name)
            print(row)

    db.close()
