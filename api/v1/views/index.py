#!/usr/bin/python3
from flask import jsonify
import app_views from api.v1.views

app_views.route('/status', methods=['GET'])

def status():
    """Returns a JSON: status: OK"""
    return jsonify({"status": "OK"})
