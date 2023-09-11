# create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
# print(temperature)

# import pandas
#
# data = pandas.read_csv("weather-data.csv")
# # temp_list = data["temp"].to_list()
# # avg = sum(temp_list) / len(temp_list)
#
# monday = data[data.day == "Monday"]
# # (0°C × 9/5) + 32 = 32°F
# monday_temp_f = (monday.temp * 9 / 5) + 32
# print(monday_temp_f)

import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "fur color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(color_dict)
print(df)