#!/usr/bin/python3
""" Index view
"""
from flask import jsonify
from models import storage

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """ get objects counts """

    return jsonify(storage.count())
