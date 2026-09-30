from flask import Flask, render_template, request
import pandas as pd
import joblib
import sys
import json
from pathlib import Path

import streamlit as st

app = Flask(__name__)

# Charger le pipeline
model = joblib.load('model.pkl')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Récupération des données
    data = {
        "G1": float(request.form["G1"]),
        "G2": float(request.form["G2"]),
        "failures": float(request.form["Failures"]),
        "studytime": float(request.form["Study time"]),
        "freetime": float(request.form["Freetime"]),
        "Medu": float(request.form["Medu"]),
        "Fedu": float(request.form["Fedu"]),
        "absences": float(request.form["Absences"]),
        "age": float(request.form["Age"]),
        "schoolsup": request.form["School sup"],
        "higher": request.form["Higher"]
    }

    # DataFrame avec exactement les features du modèle
    input_data = pd.DataFrame([data])

    # Prédiction
    prediction = model.predict(input_data)[0]

    # Limiter l'affichage à 2 décimales
    prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)
