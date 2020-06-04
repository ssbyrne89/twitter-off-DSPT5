
# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/") ###navigator decorator
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about") ###navigator decorator
def about():
    return "About me"