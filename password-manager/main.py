# # Day 30 - Intermediate - Errors, Exceptions and JSON Data Improving the Password
# # 001 Day 30 Goals what you will make by the end of the day
# # 002 Catching Exceptions The try catch except finally Pattern
# # FileNotFond

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdsafs"])  # after 2 times run the code then change "sdsafs" to "key" and run again
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:  # When all of "try" section goes successfully then jump to this section.
#     content = file.read()
#     print(content)
# finally:  # Run no matter what happened.
#     file.close()
#     print("File was closed.")

# # 003 Raising your own Exceptions

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

# # 004 [Interactive Coding Exercise] IndexError Handling

# fruits = ["Apple", "Pear", "Orange"]
#
#
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)

# # 005 [Interactive Coding Exercise] KeyError Handling

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass  # OR total_likes += 0

print(total_likes)
