# File Not Fond

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdsafs"])  # after 2 times run the code then change "sdsafs" to "key" and run again
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:  # When all of "try" section goes successfully then jump to this section.
    content = file.read()
    print(content)
finally:  # Run no matter what happened.
    file.close()
    print("File was closed.")
