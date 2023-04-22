import sqlite3

connection = sqlite3.connect('aufgaben.db')

sql_create = "Create table aufgaben (aufgaben_id INTEGER PRIMARY KEY AUTOINCREMENT, wochentag TEXT NOT NULL, name TEXT NOT NULL, uhrzeit TEXT NOT NULL, datum_abgabe_tag TEXT NOT NULL, datum_abgabe_monat TEXT NOT NULL)"


connection.execute(sql_create)

connection.commit()
connection.close()
