# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#         #print(row)
#     print(temp)

import pandas as pd
data = pd.read_csv("weather_data.csv")
# print(data["temp"].mean())
# print(sum(data["temp"])/ len(data["temp"]))
# print(data[data.temp == data["temp"].max()])

mon = data[data.day == "Monday"]
print((int(mon.temp)*9/5)+32)

data_dict = {
    "students" : ["Amy", "james", "Akash"],
    "scores": [76 ,77 ,78]
}

print(pd.DataFrame(data_dict))