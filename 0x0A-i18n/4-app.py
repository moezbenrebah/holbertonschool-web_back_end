#!/usr/bin/env python3
"""flask application"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext
Config = __import__('1-app').Config


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Determine the best match with our supported languages. """
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    locale = request.accept_languages.best_match(Config.LANGUAGES)
    return locale


app.config.from_object('4-app.Config')


@app.route('/')
def default() -> str:
    """ Returns a 4-index.html template """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
