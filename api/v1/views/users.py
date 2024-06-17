#!/usr/bin/python3
""" Users view
"""
from flask import jsonify, make_response, request, abort
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """ Get list of all users
    """

    users = storage.all(User).values()

    user_list = []
    for user in users:
        user_list.append(user.to_dict())

    return make_response(jsonify(user_list), 200)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_a_user(user_id):
    """ Get a single user
    """

    user = storage.get(User, user_id)

    if user is None:
        abort(404)

    return make_response(jsonify(user.to_dict()), 200)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_user(user_id):
    """ Delte a state
    """

    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_a_user():
    """ Create a user
    """

    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    data = request.get_json()
    if 'email' not in data:
        return make_response(jsonify({"error": "Missing email"}), 400)

    if 'password' not in data:
        return make_response(jsonify({"error": "Missing password"}), 400)

    instance = User(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_a_user(user_id):
    """ Update a user
    """

    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    skip = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()

    for key, value in data.items():
        if key not in skip:
            setattr(user, key, value)
    storage.save()

    return make_response(jsonify(user.to_dict()), 200)
