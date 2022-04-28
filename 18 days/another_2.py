import turtle as t
import random

tim = t.Turtle()

tim.speed("fastest")
t.colormode(255)

def random_color():
    # color_options= ["aquamarine", "pale green", "light pink", "powder blue", "dodger blue", "tomato"]
    # tim.color(random.choice(color_options))
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tim.color(r, g, b)
    return

def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        random_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()