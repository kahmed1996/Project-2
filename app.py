from flask import Flask, render_template, current_app

app = Flask(__name__)

hello_dict = {"Hello": "World!"}


@app.route("/")
def home():
  return "Climate and Population Analysis"

@app.route('/index')
def index():
   return render_template("index.html") 







if __name__ == "__main__":
    app.run(debug=True)
