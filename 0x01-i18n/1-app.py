#!/usr/bin/env python3
""" module for application i18n and i10n """
from flask import Flask, render_template
from flask_babel import Babel, gettext as _

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ class for configurition """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello():
    """ Route home directory """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
