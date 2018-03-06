from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route("/index/")
def home():
    return "Hi there"


@app.route("/SayHello/<user>/")
def hello(user):
    return "Hello " + user


app.run()
