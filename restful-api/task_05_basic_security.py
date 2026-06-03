#!/usr/bin/python3
"""Flask API Security with Basic Auth + JWT"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# USERS IN MEMORY
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ---------------- BASIC AUTH ----------------

@auth.verify_password
def verify(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ---------------- JWT LOGIN ----------------

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 401

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 401

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad credentials"}), 401

    token = create_access_token(identity={
        "username": username,
        "role": user["role"]
    })

    return jsonify({"access_token": token})


# ---------------- JWT PROTECTED ----------------

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ---------------- ADMIN ONLY ----------------

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()

    if identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ---------------- ERROR HANDLING ----------------

@jwt.unauthorized_loader
def missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token(err, _):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token(err, _):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
