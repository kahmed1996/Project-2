from flask import Flask, render_template, current_app, url_for

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


 
if __name__ == "__main__":
    app.run(debug=True)
