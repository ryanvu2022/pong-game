from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 70, "normal")
SCOREBOARD_COLOR = "#15f045"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, False, ALIGNMENT, FONT)
        self.goto(100, 200)
        self.write(self.right_score, False, ALIGNMENT, FONT)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
