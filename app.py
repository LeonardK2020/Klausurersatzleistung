import sqlite3
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap = Bootstrap(app)

@app.route("/")

def startseite():
    connection = sqlite3.connect('aufgaben.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name, datum_abgabe_tag, datum_abgabe_monat FROM aufgaben;")
    aufgaben = cursor.fetchall()
    connection.close()
    connection = sqlite3.connect('termine.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name, datum_tag, datum_monat, datum_jahr, wochentag, uhrzeit_anfang, uhrzeit_ende FROM termine;")
    aufgaben = cursor.fetchall()
    connection.close()
    return render_template("index.html", aufgaben=aufgaben)



@app.route("/Aufgaben")

def Aufgaben():
    return render_template("Aufgaben.html")


@app.route("/newTask", methods=["POST"])
def newTask():
    if request.method == 'POST':
        connection = sqlite3.connect('aufgaben.db')
        cursor = connection.cursor()
        aufgaben_name = request.form.get('name')
        aufgaben_tag = request.form.get('aufgaben_tag')
        aufgaben_monat = request.form.get('aufgaben_monat')
        
        try:
            connection.execute("INSERT INTO aufgaben (name, datum_abgabe_tag, datum_abgabe_monat) VALUES (?, ?, ?);", (aufgaben_name, aufgaben_tag, aufgaben_monat))
            connection.commit()
            connection.close()
            return "Die Aufgabe wurde erfolgreich hinzugefügt."
        except sqlite3.Error as error:
            return "Es gab ein Problem beim Hinzufügen dieser Aufgabe." + str(error)
        

    return render_template("Aufgaben.html")


@app.route("/Kalender")

def Kalender():
    return render_template("Kalender.html")

@app.route("/Termine")
def Termine():
    return render_template("Termine.html")

@app.route("/newDate")
def newDate():
    if request.method == 'POST':
        connection = sqlite3.connect('termine.db')
        cursor = connection.cursor()
        termin_name = request.form.get('name')
        datum_tag = request.form.get('datum_tag')
        datum_monat = request.form.get('datum_monat')
        datum_jahr = request.form.get('datum_jahr')
        termin_wochentag = request.form.get('wochentag')
        uhrzeit_anfang = request.form.get('uhrzeit_anfang')
        uhrzeit_ende = request.form.get('uhrzeit_ende')

        try:
            connection.execute("INSERT INTO termine (name, datum_tag, datum_monat, datum_jahr, wochentag, uhrzeit_anfang, uhrzeit_ende ) VALUES (?, ?, ?, ?, ?, ?, ?);", (termin_name, datum_tag, datum_monat, datum_jahr, termin_wochentag, uhrzeit_anfang, uhrzeit_ende))
            connection.commit()
            connection.close()
            return "Der Termin wurde erfolgreich hinzugefügt."
        except sqlite3.Error as error:
            return "Es gab ein Problem beim Hinzufügen dieses Termins." + str(error)
    return render_template("Termine.html")

@app.route("/login")

def login():
    return render_template("login.html")

if __name__ == '__main__':  

    app.run(debug=True)

#datenbank Befehle
#connection = sqlite3.connect('user.db')
#connection.execute()
#connection.commit()
#connection.close()