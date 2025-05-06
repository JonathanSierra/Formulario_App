from flask import Flask, request, jsonify, render_template

from flask_cors import CORS

from dotenv import load_dotenv

import os

from pymongo import MongoClient


load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["formularioCustomers"]
collection = db["customers"]

def createApp():
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"mensaje":"API funcionando correctamente"}), 200

    @app.route("/guardar", methods=["POST"])
    def guardar():
        try:
            data = request.get_json()
            firstNames = data["firstNames"]
            lastNames = data["lastNames"]
            email = data["email"]
            phoneNumber = data["phoneNumber"]
            date = data["date"]

            collection.insert_one({
                "firstNames": firstNames,
                "lastNames": lastNames,
                "email": email,
                "phoneNumber": phoneNumber,
                "birthDate": date
            })

            return jsonify({"mensaje": "Datos guardados con exito"}), 200

        except Exception as e:
            import traceback
            print("Error al guardar en MongoDB:", e)
            traceback.print_exc()
            return jsonify({"error": "Error al guardar datos"}), 500
    
    return app


if __name__ == "__main__":
    app = createApp()
    app.run(debug=True)
