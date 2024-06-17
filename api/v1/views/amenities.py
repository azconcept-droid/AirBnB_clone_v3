#!/usr/bin/python3
""" Amenities view
"""
from flask import jsonify, make_response, request, abort
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_all_amenities():
    """ Get list of all Amenity
    """

    all_amenities = storage.all(Amenity).values()
    amenity_list = []

    for amenity in all_amenities:
        amenity_list.append(amenity.to_dict())

    return jsonify(amenity_list)


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_an_amenity(amenity_id):
    """ Get an amenity
    """

    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_an_amenity(amenity_id):
    """ Delte an amenity
    """

    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)

    storage.delete(amenity)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_an_amenity():
    """ Create an amenity
    """

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()

    instance = Amenity(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def modify_an_amenity(amenity_id):
    """ Modify an amenity
    """

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    skip = ['id', 'created_at', 'updated_at']

    data = request.get_json()

    for key, value in data.items():
        if key not in skip:
            setattr(amenity, key, value)
    storage.save()

    return make_response(jsonify(amenity.to_dict()), 200)
