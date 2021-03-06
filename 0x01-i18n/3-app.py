#!/usr/bin/env python3
""" module for application i18n and i10n """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = "This is a doc adding to gettext"
""" instantiate the Babel object """


class Config(object):
    """ class for configurition """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" use Config class for configurition """


@app.route('/')
def hello():
    """ Route home directory """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ get locale function """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.debug = True
    app.run()
