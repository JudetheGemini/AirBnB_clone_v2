#!/usr/bin/python3
"""
    Python script with two routes
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
        Displays 'Hello HBNB!' in the browser
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
        Displays 'HBNB' in the browser
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def variable(text):
    """
        Displays 'C' followed by teh value of the text variable
    """
    return f"C {text}".replace('_', ' ')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
