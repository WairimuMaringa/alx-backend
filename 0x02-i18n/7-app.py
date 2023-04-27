#!/usr/bin/env python3
"""
Define a get timezone function
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz.exceptions
from pytz import timezone


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Class configuration. """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """ output the message. """
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """ Get fmatch locale based on request. """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Gives correct timezone. """
    t_zone = request.args.get('timezone', None)

    if t_zone:
        try:
            return timezone(t_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'

    default = app.config['BABEL_DEFAULT_TIMEZONE']

    return request.accept_languages.best_match(default)


def get_user():
    """ Output the user"""
    user_id = request.args.get('login_as')

    if user_id is None:
        return None

    return users.get(int(user_id))


@app.before_request
def before_request():
    """sets a user object to flask.g"""
    user = get_user()
    g.user = user


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
