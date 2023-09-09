import pandas

# data = pandas.read_csv("weather-data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# # average
# print((sum(temp_list))/len(temp_list))
#
# print(data["temp"].mean())

# # max value
# print(data["temp"].max())

# # get data in columns
# print(data["temp"])
# print(data.temp)

# # get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# # __________
# import pandas
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
# ex_data = data["Primary Fur Color"].value_counts()
#
# data_frame = pandas.DataFrame(ex_data)
# data_frame.to_csv("squirrel_count.csv")
# # __________

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")