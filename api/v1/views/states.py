#!/usr/bin/python3
""" States view
"""
from flask import jsonify, make_response, request
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """ Get list of all state
    """

    print(State)

    return jsonify({})


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_a_state(state_id):
    """ Get a single state
    """

    if storage.get(State, state_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)
    print(storage.get(State, state_id))

    return jsonify({})


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_a_state(state_id):
    """ Delte a state
    """

    if storage.get(State, state_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    storage.delete(storage.get(State, state_id))

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_a_state():
    """ Create a state
    """

    State.save()
    return make_response(jsonify({}), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def modify_a_state(state_id):
    """ Modify a state
    """

    if storage.get(State, state_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    State.save()
    return make_response(jsonify({}), 200)
