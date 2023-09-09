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
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")