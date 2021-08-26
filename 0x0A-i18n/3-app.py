#!/usr/bin/env python3
"""route module"""

from flask import Flask, request, render_template
from flask_babel import Babel, _
#Config = __import__('1-app').Config


app = Flask(__name__)
babel = Babel(app)


#@babel.localeselector
#def get_locale():
#    """match the best language to support"""
#    return request.accept_languages.best_match(Config.LANGUAGES)


#app.config.from_object('3-app.Config')


@app.route('/')
def index():
    """display 3-index.html"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
