from flask import Flask, render_template, current_app, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import sys
import json
from flask_heroku import Heroku
import numpy as np

app = Flask( __name__ )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

heroku = Heroku(app)
db = SQLAlchemy(app)
# db.create_all()


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

class Dataentry(db.Model):
	__tablename__ = "data"
	date = db.Column(db.String, primary_key=True)
	anchorage = db.Column(db.Integer)
	chicago = db.Column(db.Integer)
	fort_wayne = db.Column(db.Integer)
	louisville = db.Column(db.Integer)
	detroit = db.Column(db.Integer)	
	minneapolis = db.Column(db.Integer)
	new_york_city = db.Column(db.Integer)
	cleveland = db.Column(db.Integer)
	snow = db.Column(db.Integer)
	phoenix = db.Column(db.Integer)
	los_angeles = db.Column(db.Integer)	
	san_diego = db.Column(db.Integer)
	miami = db.Column(db.Integer)
	atlanta = db.Column(db.Integer)
	honolulu = db.Column(db.Integer)
	nashville = db.Column(db.Integer)
	corpus_christi = db.Column(db.Integer)
	houston = db.Column(db.Integer)
	las_vegas = db.Column(db.Integer)
	nosnow  = db.Column(db.Integer)
	
	def __init__ (self, mydata):
		self.date=date
		self.anchorage=anchorage
		self.chicago=chicago
		self.fort_wayne=chicago
		self.louisville=louisville
		self.detroit=detroit,
		self.minneapolis=minneapolis
		self.new_york_city=new_york_city
		self.cleveland=cleveland
		self.snow=snow
		self.phoenix=phoenix
		self.los_angeles=los_angeles
		self.san_diego=los_angeles
		self.miami=miami
		self.atlanta=atlanta
		self.honolulu=honolulu
		self.nashville =nashville
		self.corpus_christi=corpus_christi
		self.houston=houston
		self.las_vegas=las_vegas
		self.nosnow=nosnow

   
@app.route("/dbreturn")
def dbreturn():
	results = db.session.query(Dataentry.date,Dataentry.snow,Dataentry.nosnow).all()
	# Convert list of tuples into normal list
	citypopsz = list(np.ravel(results))
	return jsonify(citypopsz)

@app.route("/submit", methods=["POST"])
def post_to_db():
    indata = Dataentry(request.form['mydata'])
    data = copy(indata. __dict__ )
    del data["_sa_instance_state"]
    try:
        db.session.add(indata)
        db.session.commit()
    except Exception as e:
        print("\n FAILED entry: {}\n".format(json.dumps(data)))
        print(e)
        sys.stdout.flush()
    return 'Success! To enter more data, <a href="{}">click here!</a>'.format(url_for("enter_data"))
    
@app.route("/dataentry")
def enter_data(): 
    return render_template("dataentry.html")

 
if __name__ == "__main__":
    app.run(debug=True)
