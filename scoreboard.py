from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
        self.hideturtle()

    def score_tracking(self, Score):
        self.score = Score
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
