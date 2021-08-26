#!/usr/bin/env python3
""""""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """configure available languages in the app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object("1-app.Config")


@app.route('/')
def index():
    """display 1-index.html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
