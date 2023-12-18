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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_list(id=None):
    """
    States display
    """
    states = [state for state in storage.all(State).values()]
    print(states[0].to_dict()['id'])
    hasId = False
    if id :
        states = [state for state in states if state.to_dict()["id"] == id]
        if len(states) != 0:
            hasId = True
    print(hasId)
    return render_template('9-states.html', states=states, id=id, hasId= hasId)


if __name__ == '__main__':
    app.run(debug=False)
