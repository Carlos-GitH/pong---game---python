from turtle import Screen
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1 = Paddle1()
paddle2 = Paddle2()
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(paddle1.move_up, "a")
screen.onkeypress(paddle1.move_down, "d")
screen.onkeypress(paddle2.move_up, "Right")
screen.onkeypress(paddle2.move_down, "Left")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() < -355 or ball.distance(paddle2) <50 and ball.xcor() > 355:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.default_position()
        score.paddle1_point()

    if ball.xcor() < -380:
        score.paddle2_point()
        ball.default_position()

screen.exitonclick()
