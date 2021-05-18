import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


def gen_table(poet_dataframe):
    space = "            "
    std = ""

    for i in range(0, len(poet_dataframe)):
        name = list(poet_dataframe['姓名'])[i]
        routine = list(poet_dataframe['平时成绩'])[i]
        midterm = list(poet_dataframe['期中成绩'])[i]
        final = list(poet_dataframe['期末成绩'])[i]
        total = list(poet_dataframe['总成绩'])[i]

        color = "green" if total > 84 else ("red" if total < 60 else "yellow")

        std_format = f"<tr><td>{name}</td><td>{routine}</td><td>{midterm}</td><td>{final}</td><td>{total}</td><td>" \
                     f"<div class='stateDiv' style='background-color:{color}; width:{total}px'></div>" \
                     f"</td></tr>\n"
        std += (space + std_format)

    return std


@app.route("/", methods=("get",))
def act():
    typ = request.args.get("type")
    order = request.args.get("order")

    if typ is not None and order is not None:
        mtd = f"排序方式：{typ} {order}"
        order = (order == "升序")

        poet_data_sorted = poet_data.sort_values(by=typ, ascending=order)
    else:
        mtd = "排序方式：未有效指定"
        poet_data_sorted = poet_data

    return render_template("stud.html", stu_data=gen_table(poet_data_sorted), stu_ord=mtd)


def initialize():
    poet_data['总成绩'] = round(poet_data['平时成绩'] * 0.3 + poet_data['期中成绩'] * 0.3 + poet_data['期末成绩'] * 0.4)
    poet_data['总成绩'] = poet_data['总成绩'].astype(int)


if __name__ == "__main__":
    poet_data = pd.read_csv("data/poetScore.txt")
    initialize()

    app.run("0.0.0.0", port=5000, debug=True)
