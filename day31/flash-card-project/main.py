from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_lo_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["French"]
    flash.itemconfig(title_text, text="French", fill="black")
    flash.itemconfig(word_text, text=current_card["French"], fill="black")
    flash.itemconfig(flash_image, image=flash_image_front)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    flash.itemconfig(flash_image, image=flash_image_back)
    flash.itemconfig(title_text, text="English", fill="white")
    flash.itemconfig(word_text, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn, index=False)
    data.to_csv("data/words_to_learn.csv")
    next_card()

window = Tk()
window.title("Flash Card Game")
#window.setup(width=800, height=525)
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50,pady=50)
flip_timer = window.after(3000, func=flip_card)
flash_image_front = PhotoImage(file=r"images/card_front.png")
flash_image_back = PhotoImage(file=r"images/card_back.png")
flash = Canvas(width=800, height=526)
flash_image = flash.create_image(400,263,image=flash_image_front)
flash.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title_text = flash.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = flash.create_text(400, 283, text="", font=("Ariel", 60, "bold"))
flash.grid(row=0,column=0,columnspan=2)

x_image = PhotoImage(file=r"images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command = next_card)
x_button.grid(row=1,column=0)

r_image = PhotoImage(file=r"images/right.png")
r_button = Button(image=r_image, highlightthickness=0, command=is_known)
r_button.grid(row=1,column=1)

next_card()
window.mainloop()