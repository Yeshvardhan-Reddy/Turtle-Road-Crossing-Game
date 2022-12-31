from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Crossing Game")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car = Cars()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")

game_on = True
while game_on:
    car.create_car()
    car.move()
    time.sleep(.1)
    screen.update()
    for x in car.cars:
        if player.distance(x) < 20:
            game_on = False
            scoreboard.game_over()
    if player.ycor() == 240:
        scoreboard.level_up()
        player.start_line()
        car.next_level()


screen.exitonclick()
