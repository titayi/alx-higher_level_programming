#!/usr/bin/python3
""" Module MySQLdb """
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3]
        )
    except MySQLdb.Error:
        print("Error Connecting...")
    cur = db.cursor()
    try:
        cur.execute("SELECT cities.name FROM cities INNER JOIN\
                     states ON cities.state_id = states.id WHERE\
                     states.name = %s ORDER BY cities.id", (sys.argv[4],))
        results = cur.fetchall()
        for result in results:
            print(result)
    except MySQLdb.Error:
        print("Execution failed")
    cur.close()
    db.close()
