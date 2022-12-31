from turtle import Turtle

FONT = ("courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.n = 1
        self.color("black")
        self.goto(0, 260)
        self.write(arg=f"Level: {self.n}", align="center", font=FONT)

    def level_up(self):
        self.n += 1
        self.clear()
        self.write(arg=f"Level: {self.n}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)


