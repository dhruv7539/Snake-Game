from turtle import Turtle


start_pos = [(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in start_pos:
            self.add_segments(position)

    def add_segments(self,position):
        new = Turtle(shape='square')
        new.color('white')
        new.penup()
        new.goto(position)
        self.segments.append(new)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]


    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[seg - 1].xcor()
            y_new = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_new, y_new)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
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