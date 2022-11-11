#!/usr/bin/python3
"""
    Python script that creates a simple route
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
        Returns a text to the browser when route is visited
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
