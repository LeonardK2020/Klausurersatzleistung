import sqlite3

connection = sqlite3.connect('datenbank.db')

sql_create1 = "Create table aufgaben  (aufgaben_id INTEGER PRIMARY KEY AUTOINCREMENT, datum TEXT ,  name TEXT, uhrzeit TEXT ,  datum_abgabe_tag TEXT , datum_abgabe_monat TEXT, priorität TEXT, benutzer_id INTEGER ,FOREIGN KEY(benutzer_id) REFERENCES benutzer(benutzer_id) )" 
sql_create2 = "Create table benutzer (benutzer_id INTEGER PRIMARY KEY AUTOINCREMENT, vorname TEXT , nachname TEXT, benutzername TEXT , passwort TEXT )" 
sql_create3 = "Create table termine (termin_id INTEGER PRIMARY KEY AUTOINCREMENT, datum_tag INTEGER , datum_monat INTEGER , datum_jahr INTEGER , wochentag TEXT , name TEXT , uhrzeit_anfang TEXT, uhrzeit_ende TEXT, benutzer_id INTEGER ,FOREIGN KEY(benutzer_id) REFERENCES benutzer(benutzer_id) )"


connection.execute(sql_create1)
connection.execute(sql_create2)
connection.execute(sql_create3)

connection.commit()
connection.close()