from turtle import Turtle, Screen, penup, pendown
import turtle as t
import random

tim = Turtle()
t.colormode(255)
tim.shape("turtle")


# for _ in range(10):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
color = ["blue", "green yellow", "orange red", "moccasin"]
walk = [0, 90, 180, 270]
# def shape(side):
#     angle = 360/side
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(angle)
#
# for i in range(3,11):
#     tim.color(random.choice(color))
#     shape(i)

# tim.width(10)
tim.speed(40)
# while True:
#     tim.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     tim.forward(30)
#     tim.setheading(random.choice(walk))

def spirograph(gap):
    for i in range(int(360/gap)):
        tim.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

spirograph(5)
# print(random.choice(walk))
screen = Screen()
screen.exitonclick()

