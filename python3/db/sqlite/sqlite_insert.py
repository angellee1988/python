#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect('data/test.db')

cursor = conn.cursor()

# sql = 'insert into user (id, name) values (2, 小明)'
# cursor.execute(sql)
# cursor.execute('insert into user (id, name) values (\'10\', \'小明\')')

for i in range(100, 110):
    sql = 'insert into user (id, name) values (%s, %s)'
    data = (str(i), str(i))
    cursor.execute(sql % data)
print(cursor.rowcount)

cursor.close()
conn.commit()
conn.close()
