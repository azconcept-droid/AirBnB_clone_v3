#!/usr/bin/python3
""" Citys view
"""
from flask import jsonify, make_response, request
from models.state import State
from models.city import City
from models import storage
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_all_cities(state_id):
    """ Get list of all cities in a state
    """

    if storage.get(State, state_id) == None:
        return make_response(jsonify({"error": "Not found"}), 404)

    return jsonify({})


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_a_city(city_id):
    """ Get a single city
    """

    if storage.get(City, city_id) == None:
        return make_response(jsonify({"error": "Not found"}), 404)
    print(storage.get(City, city_id))

    return jsonify({})

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_a_city(city_id):
    """ Delte a city
    """

    if storage.get(City, city_id) == None:
        return make_response(jsonify({"error": "Not found"}), 404)

    storage.delete(storage.get(City, city_id))

    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_a_state(state_id):
    """ Create a city
    """

    if storage.get(State, state_id) == None:
        return make_response(jsonify({"error": "Not found"}), 404)

    City.save()
    return make_response(jsonify({}), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def modify_a_state(city_id):
    """ Modify a city
    """

    if storage.get(City, city_id) == None:
        return make_response(jsonify({"error": "Not found"}), 404)

    City.save()
    return make_response(jsonify({}), 200)
