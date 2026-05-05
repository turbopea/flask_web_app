#!/usr/bin/env python3
import pymongo
from flask import Flask, render_template, request

app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://admin:pass@mongo:27017/")
database = myclient["CV-database"]
columns = database["CVdictionary"]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        interests = request.form.get("interests")

        mydict = {"name": name, "email": email, "interests": interests}
        columns.insert_one(mydict)

    return render_template("index.html")


app.run(host="0.0.0.0", port=5000)
