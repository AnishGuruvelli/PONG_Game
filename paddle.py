# we need this paddle.py cuz we need two paddles and instead of writing the same code again, instead we create  a class

from turtle import Turtle, Screen


class Paddle(Turtle):
    # all classes start with a capital letter

    # # paddle = [height = 100, width = 100, x_pos = 350, y_pos = 0]
    # # each key press should move the paddle by 20px up and down
    # # wehn animation is turned off, the paddle gets created in the background
    # paddle = Turtle()
    # paddle.penup()
    # paddle.shape("square")
    # paddle.color("white")
    # # all turtle start by 20 by 20 and this needs to be 20 by 100 so we need to stretch it
    # paddle.shapesize(stretch_len=1, stretch_wid=5)
    # paddle.goto(350, 0)

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        # all turtle start by 20 by 20 and this needs to be 20 by 100 so we need to stretch it
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
