#!/usr/bin/python3
""" City view
"""
from flask import jsonify, make_response, request, abort
from models.state import State
from models.city import City
from models import storage
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_all_cities(state_id):
    """ Get list of all cities in a state
    """

    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    city_list = []
    for city in state.cities:
        city_list.append(city.to_dict())

    return jsonify(city_list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_a_city(city_id):
    """ Get a single city
    """

    city = storage.get(City, city_id)

    if city is None:
        abort(404)

    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_city(city_id):
    """ Delte a city
    """

    city = storage.get(City, city_id)

    if city is None:
        abort(404)

    storage.delete(city)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_a_city(state_id):
    """ Create a city
    """

    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()

    instance = City(**data)
    instance.state_id = state.id
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_a_city(city_id):
    """ Modify a city
    """
    city = storage.get(City, city_id)

    if city is None:
        abort(404)
    
    if not request.get_json():
        abort(400, description='Not a JSON')

    skip = ['id', 'created_at', 'updated_at']

    data = request.get_json()

    for key, value in data.items():
        if key not in skip:
            setattr(city, key, value)
    storage.save()

    return make_response(jsonify(city.to_dict()), 200)
