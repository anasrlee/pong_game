from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        self.goto(300,self.ycor())
        self.goto(-300,self.ycor())
