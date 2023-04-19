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