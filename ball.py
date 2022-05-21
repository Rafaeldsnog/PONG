from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.x_move = 2
        self.y_move = 2


    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def hit_wall(self):
        self.y_move *= -1

    def hit_paddle(self):
        self.x_move *= -1.5

    def left_score(self):
        self.goto(0, 0)
        self.x_move *=-1
        self.x_move = 2
        self.y_move = 2
        time.sleep(1)



    def right_score(self):
        self.goto(0, 0)
        self.x_move *=-1
        self.x_move = 2
        self.y_move = 2
        time.sleep(1)





