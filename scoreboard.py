from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_score(self, left_player, right_player):
        self.clear()
        self.goto(-100,200)
        self.write(left_player, align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(right_player, align="center", font=("Courier", 80, "normal"))



