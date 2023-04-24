import sqlite3

connection = sqlite3.connect('termine.db')

sql_create = "Create table termine (termin_id INTEGER PRIMARY KEY AUTOINCREMENT, datum_tag INTEGER, datum_monat INTEGER, datum_jahr INTEGER, wochentag TEXT, name TEXT, uhrzeit_anfang TEXT, uhrzeit_ende TEXT, benutzer_id INTEGER)"


connection.execute(sql_create)

connection.commit()
connection.close()