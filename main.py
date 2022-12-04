from flask import Flask, render_template
from flask_table import Table, Col

from tmp.tmp import db
import random

app = Flask(__name__)

class MyTable(Table):
    id = Col("ID")
    name = Col("NAME")
    spec = Col("SPECIALIZATION")
    place = Col("PLACE")
    classes = ["full-table"]

class SpecificTable(Table):
    id = Col("ID")
    name = Col("NAME")
    spec = Col("SPECIALIZATION")
    place = Col("PLACE")
    classes = ["full-table"]

names, specs, cities, items, diseases = db()

table = MyTable(items)


@app.route("/<disease>")
def disease(disease):
    new_items = []
    new_spec = random.choice(specs)
    i = 1
    for item in items:
        if item.spec == new_spec:
            new_item = item
            new_item.id = i
            new_items.append(new_item)
            i += 1
    new_table = SpecificTable(new_items)
    return render_template("diseases.html", disease=disease, new_table=new_table)

@app.route("/finddoctors")
def findDoctor():
    return render_template("finddoctor.html", table=table)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html", diseases=diseases)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
