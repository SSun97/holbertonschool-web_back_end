#!/usr/bin/env python3
""" module for application i18n and i10n """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from os import getenv

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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ get locale function """
    local_lan = request.args.get('locale')
    if local_lan in app.config['LANGUAGES']:
        return local_lan
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.debug = True
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5500")
    app.run(host=host, port=port)
