from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

DEFAULT_EMAIL = "akashbm08@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ""
    password = "".join(password_list)
    password_input.delete(0,END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def refresh():
    website_input.delete(0,END)
    password_input.delete(0,END)
    username_input.delete(0,END)
    username_input.insert(0,DEFAULT_EMAIL)

def save_details():
    new_data = {
        website_input.get() : {
            "email" : username_input.get(),
            "password" : password_input.get()
        }
    }
    if len(username_input.get()) == 0 or len(password_input.get()) == 0 or len(website_input.get()) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty")

    else:
        # is_ok = messagebox.askokcancel(title=f"{website_input.get()}", message=f"These are details entered:"
        #                                                                f"\nEmail: {username_input.get()}\n"
        #                                                                 f"Password: {password_input.get()}"
        #                                                               "\nIs it okay to save?")
        # if is_ok:

            try:
                with open("data.json", "r") as data:
                # json.dump(new_data, data,indent=4)
                    data_read = json.load(data)
                    data_read.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                with open("data.json", "w") as data:
                    json.dump(data_read, data, indent=4)
                    # data.write(f"\n{website_input.get()} | {username_input.get()} | {password_input.get()}")
            finally:
                refresh()

def search():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No File available.")
        refresh()
    else:
        if website_input.get() in data:
            email = data[website_input.get()]["email"]
            password = data[website_input.get()]["password"]
            messagebox.showinfo(title=website_input.get(), message=f"email = {email}\npassword = {password}")
        elif len(website_input.get()) == 0:
            messagebox.showerror(title="error", message="Please enter website to search")
        else:
            messagebox.showerror(title="Error", message=f"No Data available for {website_input.get()}.")
            refresh()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/ Username: ")
username_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1, sticky="EW")
username_input = Entry(width=35)
username_input.insert(0,DEFAULT_EMAIL)
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=2,row=1)
pwd_button = Button(text="Generate Password", command=generator)
pwd_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_details)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()



