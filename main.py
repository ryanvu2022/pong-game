from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_COLOR = "#150050"

screen = Screen()
screen.setup(800, 600)
screen.bgcolor(SCREEN_COLOR)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((373, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -265:
        ball.bounce_wall()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_paddle()

    if ball.xcor() > 400:
        ball.restart()
        scoreboard.left_point()

    if ball.xcor() < -410:
        ball.restart()
        scoreboard.right_point()


screen.exitonclick()


