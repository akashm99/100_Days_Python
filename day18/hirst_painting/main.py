import random
import turtle as t
# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# rgb = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb.append((r,g,b))

color_list = [(131, 165, 205), (224, 150, 101),
              (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162),
              (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47),
              (50, 111, 90), (49, 42, 47), (34, 61, 56), (227, 165, 169), (170, 188, 221), (184, 103, 112),
              (32, 59, 108), (105, 127, 160), (175, 200, 188), (33, 150, 210), (65, 66, 56)]

screen = t.Screen()
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
tim.width(20)
tim.penup()
tim.hideturtle()
tim.setheading(210)
tim.forward(350)
tim.setheading(0)
for i in range(10):
    for i in range(10):
        #tim.pencolor(random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.dot(20, random.choice(color_list))

    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)


screen.exitonclick()