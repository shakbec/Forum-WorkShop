from flask import render_template, Flask


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


app.run()
