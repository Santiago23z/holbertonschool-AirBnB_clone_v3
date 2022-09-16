#!/usr/bin/python3

import storage from models
import app_views from api.v1.views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy"""
    storage.close()


if __name__ == "__main__":
    app.run(host='HBNB_API_HOST', port='5000', threaded=True)
