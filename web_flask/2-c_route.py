#!/usr/bin/python3
"""
Module to initiate a flask
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Index route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb route
    """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    dynamic routing
    """
    text = text.replace("_", " ")
    return "C " + text

if __name__ == '__main__':
    app.run(debug=False)
