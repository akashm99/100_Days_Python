from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
bet = screen.textinput("Make bet", "Which turtle will win")


color = ["red", "green", "yellow", "blue", "purple", "black"]
ypos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(-230, ypos[i])
    all_turtles.append(tim)

def forward(turtle, speed):
    turtle.forward(speed)

if bet:
    ask = True

while ask:
    for i in all_turtles:
        if i.xcor() > 230:
            ask = False
            win = i.pencolor()
            if win == bet:
                print(f"You won. winnning turtle is {win}")
            else:
                print(f"YOu lost. winning turtle is {win}")
        speed = random.randint(1, 10)
        forward(i,speed)


screen.exitonclick()