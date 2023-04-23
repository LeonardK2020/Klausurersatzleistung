import sqlite3

connection = sqlite3.connect('benutzer.db')


cursor = connection.cursor()
select = "SELECT * FROM benutzer"

verwaltung =  cursor.execute(select).fetchall()

connection.execute(select)

print(verwaltung)


connection.close()