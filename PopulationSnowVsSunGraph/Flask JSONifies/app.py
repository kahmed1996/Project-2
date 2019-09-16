import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///titanic.sqlite")
engine = create_engine("sqlite:///citypop.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
#Passenger = Base.classes.passenger
onlytable2=Base.classes.onlytable2

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/citypop"
    )




@app.route("/citypop")
def citypop():
    """Return a list of total population of sunny vs. not sunny over time"""
    session = Session(engine)
    results = session.query(onlytable2.date,onlytable2.SNOW,onlytable2.NOSNOW).all()

    # Convert list of tuples into normal list
    citypops = list(np.ravel(results))

    return jsonify(citypops)

if __name__ == '__main__':
    app.run(debug=True)
