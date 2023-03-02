from turtle import Turtle
MOVE_DISTANCE=20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        #self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.penup()
        #self.showturtle()
    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), 250)

    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), -250)

class Paddle_A(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(-350, 0)


class Paddle_B(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(350, 0)
