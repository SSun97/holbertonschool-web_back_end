#!/usr/bin/env python3
""" create flass app """

from flask import Flask, request, jsonify, abort
from werkzeug.utils import redirect
from werkzeug.wrappers import response
# from flask.json import jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def front_page() -> str:
    """ front page """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """ Register user
    """

    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(user.email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def login() -> str:
    """ login session """

    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=['DELETE'])
def logout(session_id: str):
    """ logout session """

    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("http://0.0.0:5500")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5500")