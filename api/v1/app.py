#!/usr/bin/python3

from flask import Flask
from models import storage
from api.v1.views import app_views
<<<<<<< HEAD
from os import getenv
from flask_cors import CORS
=======
>>>>>>> ad5971e55eda90f364fd835e78d60993364d7139


app = Flask(__name__)
CORS(app, origins=['0.0.0.0'])
app.url_map.strict_slashes = False


app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def close_session(exception):
    """Closes the session"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True, debug=True)
