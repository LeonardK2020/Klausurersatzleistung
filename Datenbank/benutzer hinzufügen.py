import sqlite3

connection = sqlite3.connect('datenbank.db')
#insert="INSERT INTO benutzer(vorname, nachname, benutzername, passwort) VALUES('Antonio', 'Nemes', 'antonio', 'antoniotest')"
#insert="INSERT INTO benutzer(vorname, nachname, benutzername, passwort) VALUES('Lino', 'Lustig', 'lino', 'linotest')"
#insert="INSERT INTO benutzer(vorname, nachname, benutzername, passwort) VALUES('test1', 'fehler1', 'a', 'test1')"

connection.execute(insert)
connection.commit()
connection.close()