#!/usr/bin/env python3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


app.run(host="0.0.0.0", port=5001, debug=True)
