
with open("xxx_cnAirport.txt", mode= "r", encoding= "UTF-8") as origin_file:
    list_of_lines = origin_file.readlines()
list_of_lines.remove(list_of_lines[0])


#target_list是要求的list
target_list = []
for every_line in list_of_lines:
    items = every_line.split(",")
    
    cap18 = float(items[2])
    rate = 1 + float(items[3]) / 100
    if(rate != 0):
        cap17 = cap18 / rate
        diff_rate = rate - 1
    else: #此时无法处理
        cap17 = None 
        diff_rate = None

    target_list.append((items[1], cap18, cap17, diff_rate))

#purified是去掉同比增长率为-100%的数据（这些数据无法处理）之后的list
purified = []
for data in target_list:
    if(data[2] != None):
        purified.append(data)

purified_copy = purified
purified_copy.sort(key = lambda X:X[2], reverse = True)
idx = 1
for data in purified_copy:
    print(f"{idx},{data[0]},{data[1]},{data[2]}")
    idx += 1

purified_copy = purified
purified_copy.sort(key = lambda X:(X[2] * X[3]), reverse = True)
idx = 1
for data in purified_copy:
    print(f"{idx},{data[0]},{data[1]},{data[2]}")
    idx += 1
    
purified_copy = purified
purified_copy.sort(key = lambda X:X[3], reverse = True)
idx = 1
for data in purified_copy:
    print(f"{idx},{data[0]},{data[1]},{data[2]}")
    idx += 1
