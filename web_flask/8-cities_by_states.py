#!/usr/bin/python3
"""
Routes Hello
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states")
def states_list(strict_slashes=False):
    """states list"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
