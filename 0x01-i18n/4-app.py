#!/usr/bin/env python3
""" module for application i18n and i10n """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello():
    """ Route home directory """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ get locale function """
    local_lan = request.args.get('locale')
    if local_lan in app.config['LANGUAGE']:
        return local_lan
    else:
        return request.accept_languages.best_match(app.config['LANGUAGE'])


if __name__ == '__main__':
    app.debug = True
    app.run()
