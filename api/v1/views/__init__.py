#!/usr/bin/python3

from flask import Blueprint, render_template, abort, request, jsonify
from api.v1.views import api.v1.views.index

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
