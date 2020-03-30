#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.`name` FROM cities "
                "JOIN states ON cities.`state_id` = states.`id` "
                "WHERE states.`name` = %s "
                "COLLATE 'latin1_general_cs' "
                "ORDER BY cities.`id` ASC", (sys.argv[4],))
    print(', '.join(map(lambda x: x[0], cur.fetchall())))
    cur.close()
    db.close()
