#!/usr/bin/python3
""" Place view
"""
from flask import jsonify, make_response, request, abort
from models.place import Place
from models.city import City
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_all_places(city_id):
    """ Get list of all places in a city
    """
    city = storage.get(City, city_id)

    if city is None:
        abort(404)

    place_list = []
    for place in city.places:
        place_list.append(place.to_dict())

    return make_response(jsonify(place_list), 200)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_a_place(place_id):
    """ Get a single place
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    return make_response(jsonify(place.to_dict()), 200)


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_a_place(place_id):
    """ Delete a place
    """

    place = storage.get(Place, place_id)

    if place is None:
        abort(404)

    storage.delete(place)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_a_place(city_id):
    """ Create a place in a city
    """

    city = storage.get(City, city_id)

    if city is None:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    data = request.get_json()
    if 'user_id' not in data:
        return make_response(jsonify({"error": "Missing user_id"}), 400)

    user = storage.get(User, data['user_id'])

    if user is None:
        abort(404)

    if 'name' not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)

    instance = Place(**data)
    instance.city_id = city.id
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_a_place(place_id):
    """ Update a place
    """

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    skip = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

    data = request.get_json()

    for key, value in data.items():
        if key not in skip:
            setattr(place, key, value)
    storage.save()

    return make_response(jsonify(place.to_dict()), 200)
