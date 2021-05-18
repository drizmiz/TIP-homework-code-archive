import pandas as pd
from flask import Flask, render_template

dft = pd.read_csv("PeopleInSubwayTime.txt")
dfc = pd.read_csv("PeopleInSubwayCount.txt")

app = Flask(__name__)


@app.route("/")
def root():
    return app.send_static_file("index.html")


@app.route("/1")
def method1():
    return render_template(
        "subway1.html",
        pist_x_axis_data=list(dft["DiffInMin"]),
        pist_series_data=list(dft["人数"]),
        pisc_x_axis_data=list(dfc["时段"]),
        pisc_series_data=list(dfc["地铁内人数（时段结束时）"])
    )


@app.route("/2")
def method2():
    return app.send_static_file(
        "subway2.html"
    )


js_file = f"""
var pist_x_axis_data = {list(dft["DiffInMin"])};
var pist_series_data = {list(dft["人数"])};
var pisc_x_axis_data = {list(dfc["时段"])};
var pisc_series_data = {list(dfc["地铁内人数（时段结束时）"])};
"""

with open("./static/data.js", mode="w") as datajs:
    datajs.write(js_file)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
