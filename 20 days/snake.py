from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [[0,0],[-20,0],[-40,0]]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_body = Turtle(shape="square")
        new_body.penup()
        new_body.color("white")
        new_body.goto(position)
        self.snake_body.append(new_body)

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(self.snake_body[-1].position())

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