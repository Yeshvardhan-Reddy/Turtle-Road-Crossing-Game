from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.start_line()

    def start_line(self):
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        self.fd(20)

    def move_down(self):
        self.bk(20)
