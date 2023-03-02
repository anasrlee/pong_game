from turtle import Screen
from paddle  import Paddle_A, Paddle_B
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.title("Welcome to PyPong - Pong written in Python!")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


l_paddle= Paddle_A()
r_paddle= Paddle_B()
ball=Ball()
score=Score()

screen.listen()

screen.onkeypress(key="Up", fun=r_paddle.move_up)

screen.onkeypress(key="Down", fun=r_paddle.move_down)

screen.onkeypress(key="w", fun=l_paddle.move_up)

screen.onkeypress(key="s", fun=l_paddle.move_down)


game_is_running = True
while game_is_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# detect collision with wall
    if ball.ycor()<-280 or ball.ycor()>280:
        ball.bound()

# detect collision with paddle
    #if ball.distance(r_paddle)<50 and ball.xcor() >250 or ball.distance(l_paddle) < 50 and ball.xcor() < -250:
        #ball.reverse()
    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()

    #Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()


#detect but player1
    if ball.xcor() > 380:

        score.l_point()
        ball.reset()

#detect but player1
    if ball.xcor() <-380:

        score.r_point()
        ball.reset()


screen.exitonclick()
