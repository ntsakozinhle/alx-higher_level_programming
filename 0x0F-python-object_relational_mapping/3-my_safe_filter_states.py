#!/usr/bin/python3
import MySQLdb
import sys


def safe_filter_states(username, password, database, state_name):
    try:
        # Connect to the MySQL server
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
        # Create a cursor object
        cur = conn.cursor()

        # Construct the SQL query with parameterized query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        # Fetch all rows
        rows = cur.fetchall()

        # Fetch all rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to filter states
    safe_filter_states(username, password, database, state_name)
