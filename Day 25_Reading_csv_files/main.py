# with open("./weather_data.csv") as weather_forecast:
#     contents = weather_forecast.readlines()
#     print(contents)
#
from math import ceil

# import csv
#
# with open("weather_data.csv") as weather_forecast:
#     data = csv.reader(weather_forecast)
#     print(data)
#
#     temps = []
#     for row in data:
#         if not row[1].isdigit():
#             continue
#         else:
#             temps.append(int(row[1]))
#     print(temps)

import pandas as pd

data = pd.read_csv("weather_data.csv")
temp_list = (data["temp"]).tolist()

# avg = sum(temp_list) / len(temp_list)
# print(avg)

avg = data["temp"].mean()
# print(avg)
#
# print(data["temp"].max())

# access data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# creating a Data frame from scratch

# data_dict = {"Students": ["Misa", "Light", "Near"],
#              "Scores": [50, 0, 100]}
#
# data = pd.DataFrame(data_dict)
# data.to_csv("student_scores.csv")

# USA central park squirrel census color analysis

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors = data["Primary Fur Color"].tolist()

red = squirrel_colors.count("Cinnamon")
gray = squirrel_colors.count("Gray")
black = squirrel_colors.count("Black")

color_dict = {"Fur Color": ["Red", 'Gray', 'Black'],
              "Count": [red, gray, black]
              }

data = pd.DataFrame(color_dict)
data.to_csv("squirrel_data_now.csv")
