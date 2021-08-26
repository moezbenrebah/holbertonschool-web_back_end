#!/usr/bin/env python3
""""""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """match the best language to support"""
    return request.accept_languages.best_match(app.config['en', 'fr'])


@app.route('/')
def index():
    """display 2-index.html page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
