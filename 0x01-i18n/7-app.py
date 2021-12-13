#!/usr/bin/env python3
""" module for application i18n and i10n """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from os import getenv
import pytz

app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = "This is a doc adding to gettext"
""" instantiate the Babel object """

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ class for configurition """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" use Config class for configurition """


@babel.localeselector
def get_locale():
    """ get locale function """
    local_lan = request.args.get('locale')
    if local_lan in app.config['LANGUAGES']:
        return local_lan
    user_id = request.args.get('login_as')
    if user_id:
        local_lan = users[int(user_id)]['locale']
        if local_lan in app.config['LANGUAGES']:
            return local_lan
    local_lan = request.headers.get('locale')
    if local_lan in app.config['LANGUAGES']:
        return local_lan
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ get timezone function """
    timezone = request.args.get('timezone')
    print(timezone)
    try:
        if timezone in pytz.all_timezones:
            return timezone
    except:
        raise pytz.exceptions.UnknownTimeZoneError
    print(timezone)
    user_id = request.args.get('login_as')
    timezone = users[int(user_id)]['timezone']
    try:
        if timezone in pytz.all_timezones:
            return timezone
    except:
        raise pytz.exceptions.UnknownTimeZoneError
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """ get user return a user dictionary """
    try:
        usr_id = request.args.get('login_as')
        return users[int(usr_id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """ before request, g is only available for the lifetime of this request.
    """
    g.user = get_user()


@app.route('/')
def hello():
    """ Route home directory """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.debug = True
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5500")
    app.run(host=host, port=port)
