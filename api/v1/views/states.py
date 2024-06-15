#!/usr/bin/python3
""" States view
"""
from flask import jsonify, make_response, request, abort
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """ Get list of all state
    """

    all_states = storage.all(State).values()
    states_list = []

    for state in all_states:
        states_list.append(state.to_dict())

    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_a_state(state_id):
    """ Get a single state
    """

    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_a_state(state_id):
    """ Delete a state
    """

    state = storage.get(State, state_id) 
    if state is None:
        abort(404)

    storage.delete(state)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_a_state():
    """ Create a state
    """

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()

    instance = State(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def modify_a_state(state_id):
    """ Modify a state
    """

    state = storage.get(State, state_id) 
    if state is None:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    skip = ['id', 'created_at', 'updated_at']

    data = request.get_json()

    for key, value in data.items():
        if key not in skip:
            setattr(state, key, value)
    storage.save()

    return make_response(jsonify(state.to_dict()), 200)
