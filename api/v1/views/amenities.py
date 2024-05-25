#!/usr/bin/python3
""" Amenities view
"""
from flask import jsonify, make_response, request
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_all_amenities():
    """ Get list of all Amenity
    """

    return jsonify({})


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_an_amenity(amenity_id):
    """ Get an amenity
    """

    if storage.get(Amenity, amenity_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    return jsonify({})


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_an_amenity(amenity_id):
    """ Delte an amenity
    """

    if storage.get(Amenity, amenity_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    storage.delete(storage.get(Amenity, amenity_id))

    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_an_amenity():
    """ Create an amenity
    """

    Amenity.save()
    return make_response(jsonify({}), 201)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def modify_an_amenity(amenity_id):
    """ Modify an amenity
    """

    if storage.get(Amenity, amenity_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    Amenity.save()
    return make_response(jsonify({}), 200)
