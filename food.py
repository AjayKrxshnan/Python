from turtle import Turtle
import random
#The food class should inherit Turtle class and
# also need to have some attributes of its own
# functions used:
# turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.refresh()

    def refresh(self):
        new_x = random.randint(-250, 250)
        new_y = random.randint(-250, 250)

        self.goto(new_x,new_y)

