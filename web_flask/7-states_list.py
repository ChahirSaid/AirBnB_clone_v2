#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list")
def states_list(strict_slashes=False):
    """State list"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
