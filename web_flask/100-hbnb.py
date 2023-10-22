#!/usr/bin/python3
"""HBNB is alive"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template(
        "100-hbnb.html", states=states, amenities=amenities, places=places
    )


@app.teardown_appcontext
def teardown(exc):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
