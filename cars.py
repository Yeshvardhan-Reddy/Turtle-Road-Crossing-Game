from turtle import Turtle
import random

color = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
         "turquoise", "lightgreen", "darkgreen", "chocolate", "brown", "gray"]
MOVE_SPEED = 10
MOVE_INCREMENT = 5


class Cars:

    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_SPEED

    def move(self):
        for car in self.cars:
            car.bk(self.car_speed)

    def create_car(self):
        n = random.randint(1, 6)
        if n == 1 or n == 3:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(color))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(350, random.randint(-200, 200))
            self.cars.append(car)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT


