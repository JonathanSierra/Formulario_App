from flask import Flask, request, jsonify

from flask_cors import CORS

from dotenv import load_dotenv

import os

import mysql.connector


load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

def createApp():
    app = Flask(__name__)
    CORS(app)

    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "uck7jivl",
        database = "clientes_database"
    )

    cursor = db.cursor()

    @app.route("/guardar", methods=["POST"])
    def guardar():

        try:
            data = request.get_json()
            firstNames = data["firstNames"]
            lastNames = data["lastNames"]
            email = data["email"]
            phoneNumber = data["phoneNumber"]
            date = data["date"]

            sql = "INSERT INTO clients (firstNames, lastNames, email, phoneNumber, birthDate) VALUES (%s, %s, %s, %s, %s)"
            valores = (firstNames, lastNames, email, phoneNumber, date)
            cursor.execute(sql, valores)
            db.commit()

            return jsonify({"mensaje": "Datos guardados con exito"}), 200

        except Exception as e:
            print("Error al guardar en la base de datos:", e)
            return jsonify({"error": "Error al guardar datos"}), 500
    
    return app


if __name__ == "__main__":
    app = createApp()
    app.run(debug=True)