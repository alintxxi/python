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

with open("file1.txt") as file1:
    data1 = file1.readlines()
with open("file2.txt") as file2:
    data2 = file2.readlines()
result = [int(num) for num in data1 if num in data2 ]
print(result)

result = [int(num) for num in open("file1.txt") if num in open("file2.txt")]
print(result)

