from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)


paddle_right = Paddle((350, 0))

paddle_left = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")

screen.listen()
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

scoreboard = Scoreboard()
left_player = 0
right_player = 0
scoreboard.update_score(left_player, right_player)

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.hit_wall()

    if (ball.distance(paddle_right) < 50 and ball.xcor() > 340) or (ball.distance(paddle_left) < 50 and ball.xcor() < -340):
        ball.hit_paddle()

    if ball.xcor() > 390:
        ball.left_score()
        left_player += 1
        scoreboard.update_score(left_player, right_player)

    if ball.xcor() < -390:
        ball.right_score()
        right_player += 1
        scoreboard.update_score(left_player, right_player)


screen.exitonclick()

