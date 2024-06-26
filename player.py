from turtle import Turtle


STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.starting_position = STARTING_POSITION
        self.goto(STARTING_POSITION)

    
    def move(self):
        self.forward(MOVE_DISTANCE)


    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        

    def go_to_start(self):
        self.goto(STARTING_POSITION)