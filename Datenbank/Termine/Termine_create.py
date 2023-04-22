import sqlite3

connection = sqlite3.connect('termine.db')

sql_create = "Create table termine (termin_id INTEGER PRIMARY KEY AUTOINCREMENT, datum_tag INTEGER NOT NULL, datum_monat INTEGER NOT NULL, datum_jahr INTEGER NOT NULL, wochentag TEXT NOT NULL, name TEXT NOT NULL, uhrzeit_anfang TEXT NOT NULL, uhrzeit_anfang TEXT NOT NULL)"


connection.execute(sql_create)

connection.commit()
connection.close()