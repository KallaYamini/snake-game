from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.shape("circle")
        self.color("purple")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)



