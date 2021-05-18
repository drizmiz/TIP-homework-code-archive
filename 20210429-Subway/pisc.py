import pandas as pd

df = pd.read_csv("Subway_20180301.ppfull.txt")
series_u = df["UpClass"].value_counts()
series_d = df["DownClass"].value_counts()

dfu = pd.DataFrame(index=series_u.index, data={"上车人数": series_u.values})
dfd = pd.DataFrame(index=series_d.index, data={"下车人数": series_u.values})

category = []
blank = []
for i in range(0, 144):
    category.append(int(i))
    blank.append(int(0))
trivial_df = pd.DataFrame(index=category, data={"上车人数": blank,
                                                "下车人数": blank})

out_df = pd.merge(dfu, dfd, left_index=True, right_index=True)
out_df = out_df.combine_first(trivial_df)
out_df["上车人数"] = out_df["上车人数"].astype('int32')
out_df["下车人数"] = out_df["下车人数"].astype('int32')

out_df["净增加人数"] = out_df["上车人数"] - out_df["下车人数"]
out_df.sort_index(ascending=True)


def class_str(c: int) -> str:
    hour, seq = divmod(c, 6)
    h_str = f"{int(hour):0>2d}:"
    m_str = str(seq)
    prefix = h_str + m_str
    return prefix + "0-" + prefix + "9"


out_df.insert(0, "时段", out_df.index.map(class_str))
out_df["地铁内人数（时段结束时）"] = out_df["净增加人数"].cumsum()

out_df.to_csv("PeopleInSubwayCount.txt", index=False)

filename = "PeopleInSubwayCount.xlsx"
with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
    out_df.to_excel(writer, index=False, sheet_name="personCount")

    workbook = writer.book
    worksheet = writer.sheets["personCount"]

    chart = workbook.add_chart({"type": "line"})

    chart.add_series({"values": "=personCount!$E$2:$E$145",
                      "name": "=personCount!$E$1",
                      "categories": "=personCount!$A$2:$A$145"
                      })

    worksheet.insert_chart("G2", chart)
