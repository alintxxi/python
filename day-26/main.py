# numbers = [1, 2, 3]
# new_number = [n + 1 for n in numbers]
# print(new_number)
#
#
# name = "Angela"
# letter_list = [letter for letter in name]
# print(letter_list)
#
#
# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)
#
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# # ___[Interactive Coding Exercise] Squaring Numbers___________________________________

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # Do Not Change the code above
# # Write your 1 line code below:
# squared_numbers = [num ** 2 for num in numbers]
# # Write your code above:
# print(squared_numbers)

# # ___[Interactive Coding Exercise] Filtering Even Numbers_____________________________

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # Do Not Change the code above
# # Write your 1 line code below:
# result = [num for num in numbers if num % 2 == 0]
# # Write your code above:
# print(result)

# # ___[Interactive Coding Exercise] Data Overlap_______________________________________

# with open("file1.txt") as file1:
#     data1 = file1.readlines()
# with open("file2.txt") as file2:
#     data2 = file2.readlines()
# result = [int(num) for num in data1 if num in data2 ]
# print(result)
#
# result = [int(num) for num in open("file1.txt") if num in open("file2.txt")]
# print(result)

# # ___How to use Dictionary Comprehension______________________________________________

# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# # ___[Interactive Coding Exercise] Dictionary Comprehension 1_________________________

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't Change code above
#
# # Write your code below:
# result = {word: len(word) for (word) in sentence.split()}
#
# print(result)

# # ___[Interactive Coding Exercise] Dictionary Comprehension 2_________________________

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # Don't Change code above
#
# # Write your code below:
# weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
#
# print(weather_f)

# # ___How to Iterate over a Pandas DataFrame_________________________________________

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame:
for (key, value) in student_data_frame.items()
    print(value)

#Loop through rows of a data frame:
for (index, row) in student_data_frame.iterrows():
    print(row.student)