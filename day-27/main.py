from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # for showing label we have use "pack"

# you can change label with one of these two ways
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = Entry(width=10)
input.pack()


window.mainloop()
