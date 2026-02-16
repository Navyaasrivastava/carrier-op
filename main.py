import random
import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)
CORS(app)   # enable CORS for all routes

# ---------- Career List ----------
careers = [
    "Software Developer", "Data Scientist", "Entrepreneur",
    "Civil Engineer", "Doctor", "Digital Marketer",
    "Graphic Designer", "Psychologist", "Teacher / Professor",
    "Business Analyst", "IAS Officer", "Cyber Security Expert",
    "App Developer", "Architect", "Content Creator",
    "Banking Professional", "AI Engineer", "Lawyer",
    "Journalist", "Fashion Designer"
]

# ---------- Motivational Lines ----------
lines = [
    "You have strong potential to succeed in this field.",
    "Your personality naturally fits these careers.",
    "With focus and dedication, you can excel here.",
    "Your mindset supports growth in these domains.",
    "These paths align with your strengths and future success."
]

# ---------- ROOT ROUTE ----------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "message": "Career Prediction API is live 🚀",
        "endpoint": "/predict"
    })

# ---------- GET /predict (INFO ROUTE - prevents 404) ----------
@app.route("/predict", methods=["GET"])
def info():
    return jsonify({
        "message": "Send POST request with name, dob, place",
        "format": "DD-MM-YYYY",
        "example": {
            "name": "Yashi",
            "dob": "10-05-2003",
            "place": "Jaipur"
        }
    })

# ---------- POST /predict (MAIN API) ----------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    name = data.get("name")
    dob = data.get("dob")
    place = data.get("place")

    if not name or not dob or not place:
        return jsonify({"error": "Missing required fields"}), 400

    # Validate DOB format
    try:
        datetime.strptime(dob, "%d-%m-%Y")
    except ValueError:
        return jsonify({"error": "DOB must be in DD-MM-YYYY format"}), 400

    # Generate career suggestions
    random.seed(name + place + dob)
    suggested = random.sample(careers, 5)

    result = {
        "name": name,
        "place": place,
        "suggested_careers": suggested,
        "guidance": random.choice(lines)
    }

    return jsonify(result)

# ---------- LOCAL RUN ----------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
