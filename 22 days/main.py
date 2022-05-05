from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

paddleR = Paddle((350, 0))
paddleL= Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddleR.go_up, key="Up")
screen.onkey(paddleR.go_down, key="Down")

screen.onkey(paddleL.go_up, key="w")
screen.onkey(paddleL.go_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddleR) < 50 and ball.xcor() > 320 or ball.distance(paddleL) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
