import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
       super().__init__()
       self.color(random.choice(COLORS))
       self.shape("square")
       self.penup()
       self.shapesize(stretch_wid=1, stretch_len=2)
       self.goto(300, random.randint(-250, 250))

    def car_move(self, increment):
        self.backward(STARTING_MOVE_DISTANCE * increment)