from turtle import Turtle, Screen

tim = Turtle()
def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def move_left():
    new_heading = tim.heading() + 10
    tim.left(new_heading)

def move_right():
    new_heading = tim.heading() - 10
    tim.right(new_heading)

def draw_circle():
    tim.circle(20)

def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "d", fun = move_right)
screen.onkey(key = "d", fun = draw_circle)
screen.onkey(key = "c", fun = screen_clear)