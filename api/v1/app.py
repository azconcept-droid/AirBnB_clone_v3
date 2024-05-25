#!/usr/bin/python3
"""
Web server
"""
from flask import Flask, jsonify, make_response
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(error):
    """ close storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    # python -m api.v1.app
    host = getenv('HBNB_API_HOST') or '0.0.0.0'
    port = getenv('HBNB_API_PORT') or 5000

    app.run(host, port, threaded=True)
