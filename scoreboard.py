from turtle import Turtle

ALIGNEMENT='center'
FONT=('Arial', 24, 'normal')

class Score (Turtle):

    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,250)
        self.write(f'score: {self.l_score}', move=False, align=ALIGNEMENT, font=FONT)
        self.goto(100,250)
        self.write(f'score: {self.r_score}', move=False, align=ALIGNEMENT, font=FONT)

    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('game over', move=False, align=ALIGNEMENT, font=FONT)
