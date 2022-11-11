#!/usr/bin/python3
"""
    Python script with two routes
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
        Displays 'Hello HBNB!' in the browser
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
        Displays 'HBNB' in the browser
    """
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c(text):
    """
        Displays 'C' followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pypath(text='is cool'):
    """
        Displays 'Python' followed by value of text variable
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """
        Displays number in URL
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def html(n):
    """
        Renders a HTML page
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """
        Renders a page with a conditional statement
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
