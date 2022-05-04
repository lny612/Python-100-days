from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
# size is calculated by ration - (e.g) width = 20, height = 100 -> width = 1, height = 5
paddle.turtlesize(stretch_wid=5, stretch_len=1)

screen.listen()


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.onkey(go_up, key="Up")
screen.onkey(go_up, key="Down")

paddle.goto(350, 0)

screen.exitonclick()
