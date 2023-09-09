# create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as invited_names:
    all_names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()
    for name in all_names:
        correct_name = name.strip()
        finished_letter = starting_letter.replace("[name]", correct_name)
        with open(f"./Output/ReadyToSend/ready_to_send_{correct_name}.txt", "w") as finished_job:
            finished_job.write(finished_letter)
