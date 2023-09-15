from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))

# you can change label with one of these two ways
my_label["text"] = "New Text"
my_label.config(text="New Text", padx=50, pady=50)

# for showing label we have use "pack()" or "place()" or "grid()"
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New\nButton")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
