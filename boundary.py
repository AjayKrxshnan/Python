from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(-270, 270)
        self.pendown()
        for i in range(4):
            self.fd(540)
            self.right(90)