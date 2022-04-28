# from turtle import Turtle, Screen
# from, import = keyword/ turtle = Module name / Turtle = Thing in Module

"""
importing method:
1. import turtle : timmy = turtle.Turtle() -> timmy.forward(100)
1. from turtle import Turtle : timmy = Turtle() -> timmy.forward(100)
2. from turtle import * : no need -> forward(100)
3. import turtle as t : timmy = t.Turtle() -> timmy.forward(100)
"""

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.width(10)


def random_color():
    # color_options= ["aquamarine", "pale green", "light pink", "powder blue", "dodger blue", "tomato"]
    # tim.color(random.choice(color_options))
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tim.color(r, g, b)


def random_move():
    rand_num = random.randint(0, 1)
    if rand_num == 0:
        tim.forward(50)
    elif rand_num == 1:
        tim.backward(50)

    return


def random_direction():
    direction = [0, 90, 180, 270]
    tim.setheading(random.choice(direction))

    return

while True:
    random_color()

    tim.forward(50)
    random_direction()

