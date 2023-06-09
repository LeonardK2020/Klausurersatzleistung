import sqlite3
from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_bootstrap import Bootstrap
import time
#import flask_login
import flask
from flask_session import Session

app = Flask(__name__)
app.secret_key = b'secret key 1010'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

Bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        connection = sqlite3.connect('datenbank.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT* FROM benutzer WHERE benutzername='{name}'")
        user = cursor.fetchone()
        if user:
            session["name"] = name
            return redirect(url_for('startseite'))
        else:
            flash("Ungültiger Benutzername", "error")
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/index")
def startseite():
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name, datum, priorität, aufgaben_id FROM aufgaben;")
    aufgaben = cursor.fetchall()
    connection.close()
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name, datum_tag, datum_monat, datum_jahr, wochentag, uhrzeit_anfang, uhrzeit_ende, termin_id FROM termine;")
    termine = cursor.fetchall()
    connection.close()
    return render_template("index.html", aufgaben=aufgaben, termine=termine)

#@app.route("/login", methods=["POST", "GET"])
#def login():
#	if request.method == "POST":
#		session["name"] = request.form.get("name")
#		return redirect("/")
#	return render_template("login.html")

@app.route("/logout")
def logout():
	session["name"] = None
	return redirect("/")


@app.route("/Aufgaben")
def Aufgaben():
    return render_template("Aufgaben.html", banner=False)

@app.route("/newTask", methods=["POST"])
def newTask():
    if request.method == 'POST':
        connection = sqlite3.connect('datenbank.db')
        cursor = connection.cursor()
        aufgaben_name = request.form.get('name')
        aufgaben_datum = request.form.get('aufgaben_datum')
        #aufgaben_monat = request.form.get('aufgaben_monat')
        aufgaben_priorität = request.form.get('priorität')

        
        try:
            connection.execute("INSERT INTO aufgaben (name, datum, priorität) VALUES (?, ?, ?);", (aufgaben_name, aufgaben_datum, aufgaben_priorität))
            connection.commit()
            connection.close()
            
            #return "Die Aufgabe wurde erfolgreich hinzugefügt."
        except sqlite3.Error as error:
            return "Es gab ein Problem beim Hinzufügen dieser Aufgabe." + str(error)
        

    return render_template("Aufgaben.html", banner=True)


@app.route("/remove_aufgabe/<aufgaben_id>", methods=["GET", "POST"])
def remove_aufgabe(aufgaben_id):
    if request.method == "POST":
        connection = sqlite3.connect('datenbank.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM aufgaben WHERE aufgaben_id=?", (request.form['aufgaben_id'],))
        connection.commit()
        connection.close()
        return redirect("/")
    else:
        connection = sqlite3.connect('datenbank.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM aufgaben WHERE aufgaben_id=?", (aufgaben_id,))
        aufgabe = cursor.fetchone()
        connection.close()
        return render_template("remove_aufgabe.html", aufgabe=aufgabe)
    


@app.route('/edit_aufgabe/<aufgaben_id>', methods=['GET', 'POST'])
def edit_aufgabe(aufgaben_id):
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM aufgaben WHERE aufgaben_id=?", (aufgaben_id,))
    aufgabe = cursor.fetchone()

    if request.method == 'POST':
        name = request.form.get('name')
        aufgaben_datum = request.form.get('aufgaben_datum')
        #aufgaben_monat = request.form.get('aufgaben_monat')
        priorität = request.form.get('priorität')
        cursor.execute("UPDATE aufgaben SET name=?, datum=?, priorität=? WHERE aufgaben_id=?;", 
               (name , aufgaben_datum, priorität, aufgaben_id))        
        connection.commit()
        connection.close()
        return render_template('edit_aufgabe.html', aufgabe=aufgabe)
    else:
        connection.close()
        return render_template('edit_aufgabe.html', aufgabe=aufgabe)




@app.route("/Kalender")
def Kalender():
    return render_template("Kalender.html")


@app.route("/Termine")
def Termine():
    return render_template("Termine.html", banner=False)

@app.route("/newDate", methods=["POST"])
def newDate():
    if request.method == 'POST':
        connection = sqlite3.connect('datenbank.db')
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
    return render_template("Termine.html", banner=True)


@app.route("/remove_termin/<termin_id>", methods=["GET", "POST"])
def remove_termin(termin_id):
    if request.method == "POST":
        connection = sqlite3.connect('datenbank.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM termine WHERE termin_id=?", (request.form['termin_id'],))
        connection.commit()
        connection.close()
        return redirect("/")
    else:
        connection = sqlite3.connect('datenbank.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM termine WHERE termin_id=?", (termin_id,))
        termin = cursor.fetchone()
        connection.close()
        return render_template("remove_termin.html", termin=termin)



@app.route('/edit_termin/<termin_id>', methods=['GET', 'POST'])
def edit_termin(termin_id):
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM termine WHERE termin_id=?", (termin_id,))
    termin = cursor.fetchone()

    if request.method == 'POST':
        name = request.form.get('name')
        datum_tag = request.form.get('datum_tag')
        datum_monat = request.form.get('datum_monat')
        datum_jahr = request.form.get('datum_jahr')
        wochentag = request.form.get('wochentag')
        uhrzeit_anfang = request.form.get('uhrzeit_anfang')
        uhrzeit_ende = request.form.get('uhrzeit_ende')
        cursor.execute("UPDATE termine SET name=?, datum_tag=?, datum_monat=?, datum_jahr=?, wochentag=?, uhrzeit_anfang=?, uhrzeit_ende=? WHERE termin_id=?;", 
               (name , datum_tag, datum_monat, datum_jahr, wochentag, uhrzeit_anfang, uhrzeit_ende, termin_id))        
        connection.commit()
        connection.close()
        return render_template('edit_termin.html', termin=termin)
    else:
        connection.close()
        return render_template('edit_termin.html', termin=termin)


if __name__ == '__main__':  

    app.run(debug=True)
