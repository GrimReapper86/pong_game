from turtle import Turtle
POSITION = [(350, -40), (350, -20), (350, 0), (350, 20), (350, 40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]

    def create_paddle(self):
        for paddle_index in POSITION:
            self.add_segment(paddle_index)

    def add_segment(self, position):
        new_block = Turtle(shape='square')
        new_block.penup()
        new_block.speed("fastest")
        new_block.color('white')
        new_block.goto(position)
        self.segments.append(new_block)

    def up(self):

        for seg_number in range(len(self.segments) - 1, -1, -1):
            self.segments[seg_number].setheading(UP)
            self.segments[seg_number].forward(MOVE_DISTANCE)

    def down(self):

        for seg_number in range(len(self.segments) - 1, -1, -1):
            self.segments[seg_number].setheading(DOWN)
            self.segments[seg_number].forward(MOVE_DISTANCE)
