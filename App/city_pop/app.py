from flask import Flask, render_template, current_app, url_for, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///titanic.sqlite")
#engine = create_engine("sqlite:///citypop.sqlite")

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(engine, reflect=True)

# Save reference to the table
#Passenger = Base.classes.passenger
#onlytable2=Base.classes.onlytable2

# Create our session (link) from Python to the DB


app = Flask(__name__)

@app.route("/")
def home():
  return (#"Climate and Population Analysis<br/>"

#   f"Available Routes:<br/>"
#        f"/fifty<br/>"
#        f"/sixty<br/>"
#        f"/seventy<br/>"
#        f"/eighty<br/>"
#        f"/ninety<br/>"
#        f"/twothousand<br/>"
#        f"/twothousandten<br/>"

render_template('index.html')
)

@app.route("/fifty")
def fifty():
   return render_template("1950.html") 

@app.route("/sixty")
def sixty():
   return render_template("1960.html") 

@app.route("/seventy")
def seventy():
   return render_template("1970.html") 

@app.route("/eighty")
def eighty():
   return render_template("1980.html") 

@app.route("/ninety")
def ninety():
   return render_template("1990.html") 

@app.route("/twothousand")
def twothousand():
   return render_template("2000.html") 

@app.route("/twothousandten")
def twothousandten():
   return render_template("2010.html") 

@app.route("/citypop")
def citypop():
   return render_template("citypop.html") 

#def citypop():
#    """Return a list of total population of sunny vs. not sunny over time"""
#    session = Session(engine)
#    results = session.query(onlytable2.date,onlytable2.SNOW,onlytable2.NOSNOW).all()
#
#    # Convert list of tuples into normal list
#    citypops = list(np.ravel(results))
#
#    return jsonify(citypops)


 
if __name__ == "__main__":
    app.run(debug=True)
