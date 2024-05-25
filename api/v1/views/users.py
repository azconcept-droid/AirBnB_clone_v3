#!/usr/bin/python3
""" States view
"""
from flask import jsonify, make_response, request
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """ Get list of all users
    """

    print(User.to_dict())

    return jsonify({})


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_a_user(user_id):
    """ Get a single user
    """

    if storage.get(User, user_id) == None:
        return make_response(jsonify({"error": "Not found"}), 404)
    user_obj = storage.get(User, user_id)

    return jsonify({})


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_user(user_id):
    """ Delte a state
    """

    if storage.get(User, user_id) == None:
        return make_response(jsonify({"error": "Not found"}), 404)

    storage.delete(storage.get(User, user_id))

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_a_user():
    """ Create a user
    """

    User.save()
    return make_response(jsonify({}), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_a_user(user_id):
    """ Update a user
    """

    if storage.get(User, user_id) == None:
        return make_response(jsonify({"error": "Not found"}), 404)

    User.save()
    return make_response(jsonify({}), 200)
