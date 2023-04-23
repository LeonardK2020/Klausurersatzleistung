import sqlite3

connection = sqlite3.connect('termine.db')


cursor = connection.cursor()
select = "SELECT * FROM termine"

verwaltung =  cursor.execute(select).fetchall()

connection.execute(select)

print(verwaltung)


connection.close()