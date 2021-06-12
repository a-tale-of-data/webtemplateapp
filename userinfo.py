import sqlite3

conn = sqlite3.connect('user.db')

conn.execute('CREATE TABLE IF NOT EXISTS Users (name TEXT, email TEXT,  password TEXT,Uid INTEGER PRIMARY KEY)')
print("Created Table user")
res="Table created"
conn.close()
#crud oerations using python and sqlite3
#w3schools for html,css,js(basics)
