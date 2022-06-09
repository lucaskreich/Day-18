from turtle import Turtle, Screen, colormode
import random
# import colorgram
tim = Turtle()

tim.shape("turtle")
tim.pensize(1)
tim.speed(0)
# for y in range(3, 10):
#     y += 1
#     for i in range(y):
#         tim.forward(20)
#         tim.left(360/y)
#         tim.forward(20)
#         i += 1


# def pick_direction():
#     headings = [0, 90, 180, 270]
#     tim.setheading(random.choice(headings))


def pick_colors():

    colormode(255)

    rgb = [0, 0, 0]
    for i in range(len(rgb)):
        rgb[i] += random.randint(0, 255)
        i += 1
    tim.pencolor(rgb[0], rgb[1], rgb[2])


for i in range(100):

    tim.circle(100)
    tim.left(360/100)
    pick_colors()

# rgb_colors = []
# colors = colorgram.extract('images/Screenshot_10.png', 7)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

screen = Screen()
screen.exitonclick()
