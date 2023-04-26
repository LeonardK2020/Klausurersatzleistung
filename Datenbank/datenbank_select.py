import sqlite3

connection = sqlite3.connect('datenbank.db')


cursor = connection.cursor()
select = "SELECT * FROM aufgaben"

verwaltung =  cursor.execute(select).fetchall()

connection.execute(select)

print(verwaltung)


connection.close()