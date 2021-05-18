import pandas as pd

# 虽然不用显式import进来，但本程序还依赖xlsxwriter

with open("data/asmData.txt", mode="r", encoding="UTF-8") as asm:
    items = []
    str_lines = asm.readlines()
    for every_line in str_lines:
        items.append(list(every_line.split(sep="\t")))

instr_dict = {}
for item in items:
    # 过滤掉不符合规范的数据，去除标准是该行第1列数据的第2个字符不是数字
    if not '0' <= item[0][1] <= '9':
        continue
    # 这里strip()方法用于去除字符串前后空格
    instr_name = item[3].strip()
    if not instr_name in instr_dict:
        instr_dict[instr_name] = [1, 0]
    else:
        instr_dict[instr_name][0] += 1

    argc = len(item) - 4
    for argv in item:
        # 去除空格或换行符组成的的假参数
        for character in argv:
            if not (character == ' ' or character == '\n'):
                break
        else:
            argc -= 1

    instr_dict[instr_name][1] = max(instr_dict[instr_name][1], argc)

instr_names = list(instr_dict.keys())
instr_property = list(instr_dict.values())

instr_count = [i[0] for i in instr_property]
instr_argc = [i[1] for i in instr_property]

freq_of_instr_type = [0, 0, 0, 0]
names_of_types = ["无参指令", "单参指令", "双参指令", "多参指令"]
for index in range(0, len(instr_argc)):
    arg_cnt = min(instr_argc[index], 3)
    # 将数字更新为对应的字符串
    instr_argc[index] = names_of_types[arg_cnt]
    freq_of_instr_type[arg_cnt] += instr_count[index]

df1 = pd.DataFrame({"Instruction": instr_names, "Count": instr_count})
df2 = pd.DataFrame({"Instruction": instr_names, "Type": instr_argc})
df3 = pd.DataFrame({"Instruction": instr_names, "Amount": instr_count, "Type": instr_argc})
df4 = pd.DataFrame({"InstructionType": names_of_types, "TypeFreq": freq_of_instr_type})

df3 = df3.sort_values(by=["Amount", "Instruction"], ascending=False)

filename = "Instruction_xxx_.xlsx"

with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
    df1.to_excel(writer, index=False, sheet_name="instructionCount")
    df2.to_excel(writer, index=False, sheet_name="instructionType")
    df3.to_excel(writer, index=False, sheet_name="Summary")
    df4.to_excel(writer, index=False, sheet_name="Chart")

    workbook = writer.book
    worksheet = writer.sheets["Chart"]

    chart = workbook.add_chart({"type": "column"})

    chart.set_x_axis({"name": "指令类别"})
    chart.set_y_axis({"name": "指令出现次数"})

    chart.add_series({"values": "=Chart!$B$2:$B$5",
                      "name": "=Chart!$B$1",
                      "categories": "=Chart!$A$2:$A$5"
                      })

    worksheet.insert_chart("D2", chart)
