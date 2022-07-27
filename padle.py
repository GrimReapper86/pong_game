from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.color('white')
        self.goto(position)

    def up(self):
        new_cord = self.ycor() + 20
        self.goto(self.xcor(), new_cord)

    def down(self):
        new_cord = self.ycor() - 20
        self.goto(self.xcor(), new_cord)
