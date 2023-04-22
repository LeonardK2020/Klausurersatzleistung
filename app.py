import sqlite3
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap = Bootstrap(app)

@app.route("/")

def startseite():
    return render_template("index.html")
@app.route("/Aufgaben")

def Aufgaben():
    return render_template("Aufgaben.html")


@app.route("/newTask", methods=["POST"])
def newTask():
    if request.method == 'POST':
        connection = sqlite3.connect('aufgaben.db')
        cursor = connection.cursor()
        aufgabe_name = request.form.get('Neue Aufgabe')
        aufgabe_tag = request.form.get('Tag')
        aufgabe_monat = request.form.get('Monat')
        
        try:
            connection.execute("INSERT INTO aufgaben (name, datum_abgabe_tag, datum_abgabe_monat) VALUES (?, ?, ?);", (aufgabe_name, aufgabe_tag, aufgabe_monat))
            connection.commit()
            connection.close()
            return "Die Aufgabe wurde erfolgreich hinzugefügt."
        except sqlite3.Error as error:
            return "Es gab ein Problem beim Hinzufügen dieser Aufgabe." + str(error)
        

    return render_template("Aufgaben.html")


@app.route("/Kalender")

def Kalender():
    return render_template("Kalender.html")

@app.route("/Termin")

def Termin():
    return render_template("Termin.html")

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