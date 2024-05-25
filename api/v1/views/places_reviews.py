#!/usr/bin/python3
""" Place and review view
"""
from flask import jsonify, make_response, request
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models import storage
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def get_all_reviews(place_id):
    """ Get list of all reviews in a place
    """

    if storage.get(Place, place_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    return jsonify({})


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_a_review(review_id):
    """ Get a single review
    """

    if storage.get(Review, review_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)
    print(storage.get(Review, review_id))

    return jsonify({})


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_a_review(review_id):
    """ Delete a review
    """

    if storage.get(Review, review_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    storage.delete(storage.get(Review, review_id))

    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def create_a_review(place_id):
    """ Create a review of a place
    """

    if storage.get(Place, place_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    # if storage.get(User, user_id) is None:
    #     return make_response(jsonify({"error": "Not found"}), 404)

    Place.save()
    return make_response(jsonify({}), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_a_review(review_id):
    """ Update a review in a place
    """

    if storage.get(Review, review_id) is None:
        return make_response(jsonify({"error": "Not found"}), 404)

    Review.save()
    return make_response(jsonify({}), 200)
