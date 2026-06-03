#!/usr/bin/python3
"""Simple Flask API"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = {}


@app.route("/", methods=["GET"])
def home():
    """Home endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Status endpoint"""
    return "OK"


@app.route("/data", methods=["GET"])
def get_data():
    """Return list of usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Get user by username"""
    if username in users:
        return jsonify(users[username])

    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""

    # Check if JSON is valid
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # Check username exists in request
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check duplicate
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
