from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        # Q. how does class allow a tuple to be passed in for position when the constructor only has one variable?
        # A. Tuple is counted as one. it doesn't even have to be just tuple. it allows array, dictionary, and so on.
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # size is calculated by ration - (e.g) width = 20, height = 100 -> width = 1, height = 5
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)