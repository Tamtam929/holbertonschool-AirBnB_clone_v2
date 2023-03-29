#!/usr/bin/python3
"""script that starts a flash application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cis(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyis(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n: int):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
