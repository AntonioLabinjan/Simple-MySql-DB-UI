from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Postavke za povezivanje s bazom podataka
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'AN1246A301JA'
app.config['MYSQL_DB'] = 'Primjer'

mysql = MySQL(app)

# Funkcija za dodavanje korisnika
@app.route('/dodaj_korisnika', methods=['POST'])
def dodaj_korisnika():
    try:
        data = request.get_json()
        ime = data['ime']
        email = data['email']

        # Povezivanje s bazom podataka
        cur = mysql.connection.cursor()

        # Izvršavanje SQL upita za dodavanje korisnika
        cur.execute("INSERT INTO korisnici (ime, email) VALUES (%s, %s)", (ime, email))
        mysql.connection.commit()
        cur.close()

        response = {"message": "Korisnik je uspješno dodan."}
        return jsonify(response)

    except Exception as e:
        response = {"message": f"Greška pri dodavanju korisnika: {str(e)}"}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
