#!/usr/bin/env python3
"""Defining A Flask App"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Languages Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """gets the best language match"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """Root route"""
    home_title  = _('Welcome to Holberton')
    home_header = _('Hello world!')
    return render_template('3-index.html',
                           title=home_title,
                           header=home_header)


if __name__ == '__main__':
    app.run(debug=True)
