# coding:utf-8
from flask import Flask, render_template
import os

TEMPLATES_DIR = os.path.abspath("./templates")
STATIC_DIR = os.path.abspath("./static")
app = Flask(__name__)
app.debug=True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
