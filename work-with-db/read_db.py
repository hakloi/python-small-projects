import sqlite3

with sqlite3.connect('work-with-db/students.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
for row in rows:
    print(row)