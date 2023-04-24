import sqlite3

connection = sqlite3.connect('aufgaben.db')

sql_create = "Create table aufgaben  (aufgaben_id INTEGER PRIMARY KEY AUTOINCREMENT, wochentag TEXT ,  name TEXT NOT NULL, uhrzeit TEXT ,  datum_abgabe_tag TEXT NOT NULL, datum_abgabe_monat TEXT NOT NULL, priorität TEXT, benutzer_id INTEGER )" 
 


connection.execute(sql_create)

connection.commit()
connection.close()
