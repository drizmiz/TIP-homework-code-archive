
with open("data/ChinaAirportData.txt", mode= "r", encoding= "UTF-8") as origin_file:
    list_of_lines = origin_file.readlines()

with open("xxx_cnAirport.txt", mode = "w", encoding= "UTF-8") as output:
    output.write(list_of_lines[0])

    size = len(list_of_lines)
    index = 1
    for i in range(1, size):
        items = list_of_lines[i].split(sep = ",")
        
        airport = items[1]
        if(items[-3].isdigit()):
            annual = items[-3] + items[-2]
        else:
            annual = items[-2]
        rate = items[-1]

        if(annual != ""):
            output.write(f"{index},{airport},{annual},{rate}")
            index += 1

#与源文件不同，输出数据结尾会有一个换行，这是合理的
