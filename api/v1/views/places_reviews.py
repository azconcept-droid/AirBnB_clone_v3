#!/usr/bin/python3
""" Place and review view
"""
from flask import jsonify, make_response, request, abort
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
    place = storage.get(Place, place_id)

    if place is None:
        abort(404)

    review_list = []
    for review in place.reviews:
        review_list.append(review.to_dict())

    return make_response(jsonify(review_list), 200)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_a_review(review_id):
    """ Get a single review
    """

    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    return make_response(jsonify(review.to_dict()), 200)


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_a_review(review_id):
    """ Delete a review
    """

    review = storage.get(Review, review_id)

    if review is None:
        abort(404)

    storage.delete(review)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def create_a_review(place_id):
    """ Create a review of a place
    """
    place = storage.get(Place, place_id)

    if place is None:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    data = request.get_json()
    if 'user_id' not in data:
        return make_response(jsonify({"error": "Missing user_id"}), 400)

    user = storage.get(User, data['user_id'])

    if user is None:
        abort(404)

    if 'text' not in data:
        return make_response(jsonify({"error": "Missing text"}), 400)

    instance = Review(**data)
    instance.place_id = place.id
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_a_review(review_id):
    """ Update a review in a place
    """

    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    skip = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']

    data = request.get_json()

    for key, value in data.items():
        if key not in skip:
            setattr(review, key, value)
    storage.save()

    return make_response(jsonify(review.to_dict()), 200)
