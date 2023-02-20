import os

from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)

from decorators.protected_route import protected_route

ALGORITHMS = ["RS256"]
API_IDENTIFIER = os.getenv('API_IDENTIFIER')
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')

@app.route("/")
def index():
    """
    Default endpoint, it is public and can be accessed by anyone
    """
    return jsonify(msg="Authentication not required.")

@app.route("/dashboard")
@protected_route
def dashboard():
    """
    User endpoint, can only be accessed by an authorized user
    """
    return jsonify(msg="Authenticated.")
