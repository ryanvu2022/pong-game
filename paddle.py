from turtle import Turtle
PADDLE_COLOR = "#f56628"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(5, 1)
        self.penup()
        self.speed(0)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
