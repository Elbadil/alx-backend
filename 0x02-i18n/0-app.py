#!/usr/bin/env python3
"""Defining a Flask App"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Root route"""
    return render_template('index.html',
                           title='Welcome to Holberton',
                           h1='Hello world')


if __name__ == '__main__':
    app.run(debug=True)
