import sqlite3

with sqlite3.connect('work-with-db/students.db') as connection:
    cursor = connection.cursor()
    cursor.execute(
        "update students set name = ? where id = ?",
        ("Pasha", 2)
    )
    