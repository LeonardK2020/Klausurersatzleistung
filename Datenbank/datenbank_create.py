import sqlite3

connection = sqlite3.connect('datenbank.db')

sql_create1 = "Create table aufgaben  (aufgaben_id INTEGER PRIMARY KEY AUTOINCREMENT, wochentag TEXT ,  name TEXT NOT NULL, uhrzeit TEXT ,  datum_abgabe_tag TEXT NOT NULL, datum_abgabe_monat TEXT NOT NULL, priorität TEXT, benutzer_id INTEGER ,FOREIGN KEY(benutzer_id) REFERENCES benutzer(benutzer_id) )" 
sql_create2 = "Create table benutzer (benutzer_id INTEGER PRIMARY KEY AUTOINCREMENT, vorname TEXT NOT NULL, nachname TEXT NOT NULL, benutzername TEXT NOT NULL, passwort TEXT NOT NULL)" 
sql_create3 = "Create table termine (termin_id INTEGER PRIMARY KEY AUTOINCREMENT, datum_tag INTEGER NOT NULL, datum_monat INTEGER NOT NULL, datum_jahr INTEGER NOT NULL, wochentag TEXT NOT NULL, name TEXT NOT NULL, uhrzeit_anfang TEXT, uhrzeit_ende TEXT, benutzer_id INTEGER ,FOREIGN KEY(benutzer_id) REFERENCES benutzer(benutzer_id) )"


connection.execute(sql_create1)
connection.execute(sql_create2)
connection.execute(sql_create3)

connection.commit()
connection.close()