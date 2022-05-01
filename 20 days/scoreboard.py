from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.cnt_score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"The score is {self.cnt_score}", move=False, align=ALIGNMENT, font=FONT)

    def write_score(self):
        self.clear()
        self.cnt_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
