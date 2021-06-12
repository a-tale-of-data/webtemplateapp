import sqlite3

conn = sqlite3.connect("webtemp.db")
c = conn.cursor()
sql ='''CREATE TABLE IF NOT EXISTS Template(
   TemplateId INTEGER PRIMARY KEY,
	theme VARCHAR(20),
	color VARCHAR(30)
)'''
c.execute(sql)
c.execute('''INSERT INTO Template(
   theme, color) VALUES 
   ('Bakery', 'Red')''')

c.execute("SELECT * FROM Template")
result = c.fetchone()