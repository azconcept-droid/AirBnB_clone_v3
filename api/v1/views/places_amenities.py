#!/usr/bin/python3
""" Place and review view
"""
from flask import jsonify, make_response, request, abort
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from os import getenv


@app_views.route('/places/<place_id>/amenities',
                 methods=['GET'], strict_slashes=False)
def get_all_amenities(place_id):
    """ Get list of all amenities of a place
    """
    place = storage.get(Place, place_id)

    if place is None:
        abort(404)

    amenity_list = []
    for amenity in place.amenities:
        amenity_list.append(amenity.to_dict())

    return make_response(jsonify(amenity_list), 200)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_a_amenity(place_id, amenity_id):
    """ Delete an amenity
    """

    place = storage.get(Place, place_id)

    if place is None:
        abort(404)

    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)

    if amenity not in place.amenities:
        abort(404)

    storage.delete(amenity)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'],
                 strict_slashes=False)
def post_place_amenity(place_id, amenity_id):
    """
    Link a Amenity object to a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        if amenity in place.amenities:
            return make_response(jsonify(amenity.to_dict()), 200)
        else:
            place.amenities.append(amenity)
    else:
        if amenity_id in place.amenity_ids:
            return make_response(jsonify(amenity.to_dict()), 200)
        else:
            place.amenity_ids.append(amenity_id)

    storage.save()
    return make_response(jsonify(amenity.to_dict()), 201)
