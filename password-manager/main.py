from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
username_entry = Entry(width=43)
username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
password_entry = Entry(width=23)
password_entry.grid(column=1, row=3, sticky=W)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky=W)
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)









window.mainloop()