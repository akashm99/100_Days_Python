from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def calculate():
    output = float(input.get()) * 1.609
    label_3.config(text=f"{output}")

label_1 = Label(text="Miles")
label_1.grid(column=2,row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0,row=1)

label_3 = Label(text=f"0")
label_3.grid(column=1,row=1)

label_4 = Label(text="km")
label_4.grid(column=2,row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

input = Entry(width=7)
input.grid(column=1, row=0)

window.mainloop()
