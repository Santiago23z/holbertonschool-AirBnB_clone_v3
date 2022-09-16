#!/usr/bin/python3

<<<<<<< HEAD
from flask import Blueprint, render_template, abort, request, jsonify
from api.v1.views import api.v1.views.index
import json
import os
import models
from models import storage

=======
from flask import Blueprint
from api.v1.views.index import *
>>>>>>> ad5971e55eda90f364fd835e78d60993364d7139

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
