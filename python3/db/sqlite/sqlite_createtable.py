#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect('data/test.db')

cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.close()
conn.commit()
conn.close()
