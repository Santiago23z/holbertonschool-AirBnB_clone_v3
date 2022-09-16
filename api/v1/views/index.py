#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON status"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def stats():
    """
    /////////////////
    Call count method
    /////////////////
    """
    from models import storage
    from models.amenity import Amenity
    # from models.base_model import BaseModel, Base
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    classes = {"amenities": Amenity, "cities": City,
               "places": Place, "reviews": Review, "states": State,
               "users": User}

    result = {}
    for name, cls in classes.items():
        size = storage.count(cls)
        result.update({name: size})

    return jsonify(result)
