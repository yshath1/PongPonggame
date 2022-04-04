from turtle import Turtle

FONT_WEIGHT = "bold"
FONT_FAMILY = "exo2"
FONT_SIZE = 18
TURTLE_COLOR = "white"


class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color(TURTLE_COLOR)
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=(FONT_FAMILY, FONT_SIZE, FONT_WEIGHT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
