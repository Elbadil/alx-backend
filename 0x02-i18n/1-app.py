#!/usr/bin/env python3
"""Defining A Flask App"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """Languages Config Class"""
    LANGUAGES = ["en", "fr"]


def get_locale():
    """gets local language"""
    return request.accept_languages.best_match(Config.LANGUAGES)


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Root route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
