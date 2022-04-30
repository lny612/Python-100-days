from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.x_position = 0
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for turtle_index in range(0, 3):
            new_body = Turtle(shape="square")
            new_body.penup()
            new_body.color("white")
            new_body.goto(x=self.x_position, y=0)
            self.x_position -= 20
            self.snake_body.append(new_body)

    def move(self):
        for component in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[component - 1].xcor()
            new_y = self.snake_body[component - 1].ycor()
            self.snake_body[component].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)