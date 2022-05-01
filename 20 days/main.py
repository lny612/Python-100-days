from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # until we call update, the screen will show nothing

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # once the whole snake body finishes to move, I get my screen updated

    snake.move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.write_score()

    # detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with tail.
    for segment in snake.snake_body:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
