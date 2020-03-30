#!/usr/bin/python3
"""Script to list all states with name starting with `N` from
database `hbtn_0e_0_usa`
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE 'N%' "
                "COLLATE 'latin1_general_cs' "
                "ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
