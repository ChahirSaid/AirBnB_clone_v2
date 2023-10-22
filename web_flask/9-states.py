#!/usr/bin/python3
"""States and state"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """Display states with their cities"""
    states = storage.all(State)
    if state_id is not None:
        state_id = "State." + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(text):
    """Close"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
