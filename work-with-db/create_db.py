import sqlite3

with sqlite3.connect('work-with-db/students.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''
                   create table if not exists students (
                       id integer primary key autoincrement,
                       name text not null,
                       subject text not null
                   )
                   ''')
    
    cursor.execute(
                   "insert into students (name, subject) values (?, ?)",
                   ("Tata", "English"))
    
    cursor.execute(
        "insert into students (name, subject) values (?, ?)",
        ("Valentine", "English")
    )

print("Well done!")