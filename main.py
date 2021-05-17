from turtle import Turtle, Screen, screensize
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG Game")
screen.tracer(0)  # to turn off the animation and when we turn off the animation we have to manually turn it on
# there is a tracer function that controls the animation cuz whenever we create the paddle then it gets formed in the
# center and goes to the location i.e. 350,0

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
"""like always, make a note that when we are using a function as an input we dont add the ()"""

game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)  # the speed of the ball completely depends on how shorter we let it sleep
    # cuz the ball immediately goes to the right most corner so to make sure it goes slowly we make it sleep
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce back
        ball.bounce_y()

    # detect collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        print("made contact")
        ball.bounce_x()

    # detect collision with the l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("made contact")
        ball.bounce_x()

    # # detect collision with the paddlea
    # if (ball.distance(l_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
    #     print("made contact")
    #     ball.bounce_x()

    # detect when the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect when the left paddle misses
    # reason why these are seperate  is cuz we have to count the points too
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
