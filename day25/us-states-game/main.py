import turtle
import pandas as pd

#def get_mouse_click(x,y):
#    print(x,y)
#turtle.onscreenclick(get_mouse_click)

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guess = []
title_case = "Guess the state."
score = 0

point = turtle.Turtle()
point.hideturtle()
point.penup()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title_case, "State Name. Type exit to quit")
    for i in all_states:
        if answer_state.lower() == str(i).lower():
            guess.append(answer_state)
            all_states.remove(i)
            score += 1
            title_case = f"{score}/50 correct."
            new_x = data[data.state == i]["x"]
            new_y = data[data.state == i]["y"]
            point.goto(int(new_x), int(new_y))
            point.write(answer_state)
        elif score == 50:
            title = "You won"
            game_is_on = False
        elif answer_state == "exit":
            final = pd.DataFrame(all_states)
            final.to_csv("remaining_guesses")
            game_is_on = False
        else:
            pass

