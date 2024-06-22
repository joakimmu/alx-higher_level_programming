#!/usr/bin/env python3
import MySQLdb
import sys

def list_states(username, password, dbname):
    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=dbname,
            port=3306
        )
        cursor = db.cursor()

        # Execute the query to fetch states sorted by states.id
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        
        # Fetch all rows from the result set
        states = cursor.fetchall()
        
        # Print the states in the required format
        for state in states:
            print(state)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
    list_states(username, password, dbname)
