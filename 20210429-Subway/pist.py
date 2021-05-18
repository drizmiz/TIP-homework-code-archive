import pandas as pd

df = pd.read_csv("Subway_20180301.ppfull.txt")
dfc = df["DiffInMin"].value_counts()

out_df = pd.DataFrame({"DiffInMin": dfc.index, "人数": dfc.values})
out_df = out_df.sort_values(by="DiffInMin")

out_df.to_csv("PeopleInSubwayTime.txt", index=False)

filename = "PeopleInSubwayTime.xlsx"
with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
    out_df.to_excel(writer, index=False, sheet_name="diffCount")

    workbook = writer.book
    worksheet = writer.sheets["diffCount"]

    chart = workbook.add_chart({"type": "column"})

    chart.add_series({"values": "=diffCount!$B$2:$B$122",
                      "name": "=diffCount!$B$1",
                      "categories": "=diffCount!$A$2:$A$122"
                      })

    worksheet.insert_chart("D2", chart)
