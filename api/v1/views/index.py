#!/usr/bin/python3
""" Index view
"""
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from api.v1.views import app_views


classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """ get objects counts """

    obj_count = {}

    for cls in classes:
        obj_count[cls] = storage.count(classes[cls])

    return jsonify(obj_count)
