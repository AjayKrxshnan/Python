from turtle import Turtle,Screen
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments = []

        for position in POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.speed("fastest")
            segment.goto(position)
            self.segments.append(segment)
        self.head = self.segments[0]



    def selfCannibalCheck(self):
        for segment in self.segments[1:]:

            if self.head.distance(segment) < 10:
                 return True
        return False
    def extend(self):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.speed("fastest")
        last_segment=self.segments[len(self.segments)-1]
        new_x= last_segment.xcor()
        new_y = last_segment.ycor()
        segment.goto(new_x,new_y)
        self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
           self.head.setheading(UP)



    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

