#!/usr/bin/python3
import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    try:

        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
        cur = conn.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC LIMIT 1"
        cur.execute(query, (state_name,))

        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, database, state_name)
