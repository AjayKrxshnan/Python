from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from boundary import Boundary
screen = Screen()
screen.bgcolor("black")
screen.title("welcome to my snake game")
screen.setup(width=600,height=600)
screen.tracer(0)
snake = Snake()
food=Food()
bound = Boundary()
screen.update()

screen.listen()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
score_tracker = ScoreBoard()
while game_on:
    screen.update()
    time.sleep(0.2)
    if snake.selfCannibalCheck():
        game_on = False
        score_tracker.game_end()
        break

    snake.move()

    if (snake.head.xcor() > 260 or snake.head.xcor()< -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260):
        game_on=False
        score_tracker.game_end()
        break

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score_tracker.score_increase()
        score_tracker.score_update()





































screen.exitonclick()