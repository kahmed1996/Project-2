from flask import Flask, render_template, current_app, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from flask_heroku import Heroku
import numpy as np

app = Flask( __name__ )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

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
    __tablename__ = "dataentry"
    id = db.Column(db.Integer, primary_key=True)
    mydata = db.Column(db.Text())

    def __init__ (self, mydata):
        self.mydata = mydata


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
