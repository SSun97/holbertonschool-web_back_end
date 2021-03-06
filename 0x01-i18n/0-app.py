#!/usr/bin/env python3
""" module for application i18n and i10n """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """ Route home directory """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
