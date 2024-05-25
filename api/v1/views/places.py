#!/usr/bin/python3
""" Place view
"""
from flask import jsonify, make_response, request
from models.place import Place
from models.city import City
from models import storage
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_all_places(city_id):
    """ Get list of all places in a city
    """

    if storage.get(City, city_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    return jsonify({})


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_a_place(place_id):
    """ Get a single place
    """

    if storage.get(Place, place_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)
    print(storage.get(Place, place_id))

    return jsonify({})


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_a_place(place_id):
    """ Delete a place
    """

    if storage.get(Place, place_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    storage.delete(storage.get(Place, place_id))

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_a_place(city_id):
    """ Create a place in a city
    """

    if storage.get(City, city_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    City.save()
    return make_response(jsonify({}), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_a_place(place_id):
    """ Update a place
    """

    if storage.get(Place, place_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    Place.save()
    return make_response(jsonify({}), 200)
