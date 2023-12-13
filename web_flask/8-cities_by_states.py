#!/usr/bin/python3
"""
Module to initiate a flask
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def close_all(error):
    """
    func to remove sqlalchemy session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """
    States display
    """
    states = [state for state in storage.all(State).values()]
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(debug=False)
