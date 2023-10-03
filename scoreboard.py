from turtle import Turtle
ALIGNMENT = "center"
FONT=('mooli', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.score_update()



    def score_update(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)


    def game_end(self):
        self.goto(0,0)
        self.write("Game Over!",align=ALIGNMENT,font=FONT)
    def score_increase(self):
        self.score+=1
        self.score_update()


