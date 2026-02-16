import random
import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------- Career List ----------
careers = [
    "Software Developer","Data Scientist","Entrepreneur",
    "Civil Engineer","Doctor","Digital Marketer",
    "Graphic Designer","Psychologist","Teacher / Professor",
    "Business Analyst","IAS Officer","Cyber Security Expert",
    "App Developer","Architect","Content Creator",
    "Banking Professional","AI Engineer","Lawyer",
    "Journalist","Fashion Designer"
]

lines = [
    "You have strong potential to succeed in this field.",
    "Your personality naturally fits these careers.",
    "With focus and dedication, you can excel here.",
    "Your mindset supports growth in these domains.",
    "These paths align with your strengths and future success."
]

# ---------- Routes ----------
@app.route("/")
def home():
    return jsonify({
        "status":"running",
        "message":"Career Prediction API is live 🚀",
        "usage":"POST JSON to /predict"
    })

@app.route("/predict", methods=["GET"])
def info():
    return jsonify({
        "message":"Send POST request with name, dob, place",
        "format":"DD-MM-YYYY"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    name = data.get("name")
    dob = data.get("dob")
    place = data.get("place")

    datetime.strptime(dob, "%d-%m-%Y")

    random.seed(name + place + dob)
    suggested = random.sample(careers, 5)

    return jsonify({
        "name":name,
        "place":place,
        "suggested_careers":suggested,
        "guidance":random.choice(lines)
    })

# 🚀 IMPORTANT: This block is ONLY for local testing
if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)

