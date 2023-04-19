import sqlite3

connection =  sqlite3.connect("benutzer.db")

sql_create = "CREATE TABLE benutzer (benutzer_id INTEGER PRIMARY KEY AUTOINCREMENT, vorname TEXT NOT NULL, nachname TEXT NOT NULL, benutzername TEXT NOT NULL, passwort TEXT NOT NULL)"


connection.execute(sql_create)

connection.commit()
connection.close()
