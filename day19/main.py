from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# jim = Turtle(shape="turtle")

# tim.color("green")
# tom.color("blue")
# jim.color("red")

screen = Screen()
screen.setup(500,400)
bet = screen.textinput("Make bet", "Which turtle will win")


color = ["red", "green", "yellow", "blue", "purple"]


for  i in range
# for i in color:
#     i = Turtle(shape=f"{i}")
#
# for i in color:
#     i.penup()
# tim.penup()
# tom.penup()
# jim.penup()
# tim.goto(-230, -100)
# tom.goto(-230, 0)
# jim.goto(-230, 100)

# def back(turtle):
#     turtle.backward(10)
#
# def right(turtle):
#     turtle.right(90)
#
# def left(turtle):
#     turtle.left(90)
#
# def clear(turtle):
#     turtle.reset()

def forward(turtle, speed):
    turtle.forward(speed)


#list = [tim,tom,jim]

for i in range(30):
    speed = random.randint(1, 100)
    forward(random.choice(list), speed)

#screen.listen()
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="a", fun=left)
# screen.onkey(key="s", fun=back)
# screen.onkey(key="d", fun=right)
# screen.onkey(key="c", fun=clear)
screen.exitonclick()