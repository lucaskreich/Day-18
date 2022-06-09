
from turtle import Turtle, Screen, colormode
import random

colormode(255)

color_list = [(236, 35, 107), (146, 28, 64), (0, 255, 255), (255, 128, 0),
              (0, 0, 0), (218, 229, 235), (239, 75, 34), (6, 148, 94),
              (76, 153, 0), (204, 0, 0), (0, 0, 153), (102, 0, 51)]
tim = Turtle()
tim.penup()
tim.speed("fastest")
x = -200
y = -200
for i in range(10):
    for i in range(10):
        tim.setposition(x, y)
        tim.dot(20, random.choice(color_list))
        x += 50
    x = -200
    y += 50

screen = Screen()
screen.exitonclick()
