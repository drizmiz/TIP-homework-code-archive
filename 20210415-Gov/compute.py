# to strip the codes before and after the name of a district
def strip_to_name(line: str) -> str:
    line = line.strip().strip("0123456789")
    return line


# to keep a universal column width
def fill(string: str, width: int, chinese: bool = False, non_chinese: int = 0) -> str:
    return string + ' ' * (width - ((2 if chinese else 1) * len(string) - non_chinese))


def cp4(stat_lines: list, filename: str, mode: str = "a"):
    category = {"111": "主城区", "112": "城乡结合区", "121": "镇中心区", "122": "镇乡结合区", "123": "特殊区域",
                "210": "乡中心区", "220": "村庄"}

    head = fill("", 18, True)
    for (each_cat, its_name) in sorted(category.items()):
        head += fill(f"{its_name} ({each_cat})", 18, True, 6)

    this_province = ""
    stat_data = {}

    for each_line in stat_lines:
        # if a new provincial district starts
        if not each_line.startswith("\t"):
            this_province = strip_to_name(each_line)
        # if this line represents a grass-roots district
        if each_line.startswith("\t\t\t\t"):
            this_province_data: dict = stat_data.get(this_province, {})
            cat: str = (each_line.strip())[-3:]
            this_province_data[cat] = this_province_data.get(cat, 0) + 1
            stat_data[this_province] = this_province_data

    with open(filename, mode) as output_file:
        print(head, file=output_file)
        # ! there is no guaranteed order for provinces
        for (each_province, its_data) in stat_data.items():
            row: str = fill(each_province, 18, True)
            for each_cat in sorted(category.keys()):
                row += fill(str(its_data.get(each_cat, 0)), 18)
            print(row, file=output_file)


def cp5(stat_lines: list, filename: str, mode: str = "a"):
    provinces_of_interest = ["河南省", "内蒙古自治区"]

    this_province = ""
    stat_data = {}

    for each_line in stat_lines:
        # if a new provincial district starts
        if not each_line.startswith("\t"):
            this_province = strip_to_name(each_line)
        # if this line represents a grass-roots district
        if each_line.startswith("\t\t\t\t"):
            if this_province in provinces_of_interest:
                district_name: str = strip_to_name(each_line)
                if district_name.find("村委会") != -1:
                    district_name = district_name[: -3]
                    this_province_data: dict = stat_data.get(this_province, {})
                    for each_char in district_name:
                        this_province_data[each_char] = this_province_data.get(each_char, 0) + 1
                    stat_data[this_province] = this_province_data

    with open(filename, mode) as output_file:
        for (each_province, its_data) in stat_data.items():
            row: str = f"{each_province}："
            sorted_data: list = sorted(its_data.items(), key=lambda x: x[1], reverse=True)
            sorted_data = sorted_data[: 100]
            for (each_char, freq) in sorted_data:
                row += each_char + ' '
            print(row, file=output_file)


def cp6(stat_lines: list, filename: str, mode: str = "a"):
    last_name_str = "01李02王03张04刘05陈06杨07赵08黄09周10吴11徐12孙13胡14朱15高16林17何18郭19马20罗21梁22宋23郑24谢25韩" \
                    "26唐27冯28于29董30萧31程32曹33袁34邓35许36傅37沈38曾39彭40吕41苏42卢43蒋44蔡45贾46丁47魏48薛49叶50阎" \
                    "51余52潘53杜54戴55夏56钟57汪58田59任60姜61范62方63石64姚65谭66廖67邹68熊69金70陆71郝72孔73白74崔75康" \
                    "76毛77邱78秦79江80史81顾82侯83邵84孟85龙86万87段88漕89钱90汤91尹92黎93易94常95武96乔97贺98赖99龚100文"

    last_names = []
    for i in range(0, 99):
        last_names.append(last_name_str[3 * i + 2])
    last_names.append(last_name_str[-1])

    stat_data = {}

    for each_line in stat_lines:
        # if this line represents a grass-roots district or its direct superior
        if each_line.startswith("\t\t\t"):
            district_name: str = strip_to_name(each_line)
            district_prefix = district_name[0]
            if district_prefix in last_names:
                stat_data[district_prefix] = stat_data.get(district_prefix, 0) + 1

    with open(filename, mode) as output_file:
        for each_last_name in last_names:
            freq = stat_data[each_last_name]
            row = f"{each_last_name}\t{freq}"
            print(row, file=output_file)


if __name__ == "__main__":
    with open("xxx_StatData.txt", "r") as stat_file:
        lines = stat_file.readlines()
    f = "xxx_ComputingData.txt"
    cp4(lines, filename=f)
    cp5(lines, filename=f)
    cp6(lines, filename=f)
