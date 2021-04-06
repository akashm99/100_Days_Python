from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)


window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx = 20, pady = 20)

my_label = Label(text="This is old text")
my_label.config(text="This is new text")
my_label.grid(column=0 , row=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text = "New Button", command= button_clicked)
button2.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=4, row=3)

window.mainloop()



