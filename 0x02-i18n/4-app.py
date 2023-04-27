#!/usr/bin/env python3
"""
Implement locale
"""
from flask import, Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


class Config(object):
    """ configure given specs. """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index():
    """ display output. """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """ function and decorator. """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
