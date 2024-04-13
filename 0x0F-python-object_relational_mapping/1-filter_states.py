#!/usr/bin/python3
import MySQLdb
import sys

def filter_states(username, password, database):
   try:
        
        conn = MySQLdb.connect(host="localhost", port=3306,
                                user=username, passwd=password,
                                db=database, charset="utf8")

        cur = conn.cursor()

        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'  ORDER BY id ASC")

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
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    filter_states(username, password, database)
