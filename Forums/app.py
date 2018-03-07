from flask import render_template, Flask
import dummy_data

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=dummy_data.post_store.get_all())


app.run()
