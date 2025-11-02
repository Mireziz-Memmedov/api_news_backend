from flask import Flask, jsonify, request
from flask_cors import CORS
from .config import API_KEY
import requests

app = Flask(__name__)

CORS(app, resources={r"/api/news": {
    "origins": [
        "https://mireziz-memmedov.github.io",
        "https://didactic-space-waffle-r4w94j5rjv6xcpqj6-5500.app.github.dev"
    ],
    "methods": ["GET"]
}})

@app.route("/api/news", methods=["GET"])
def get_news():
    api_key = request.args.get("api_key")

    if api_key and api_key != API_KEY:
        return jsonify({"error": "Invalid api key"})

    try:
        url = f"https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey={API_KEY}"
        responce = requests.get(url)
        data = responce.json()
        news = data.get("articles", [])
    except Exception as e:
        news = {"error": str(e)}

    return jsonify({"news": news})