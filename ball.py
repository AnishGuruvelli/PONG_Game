from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.movespeed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.movespeed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        # cuz we want left paddle to get a turn too so we have to reverse the x axis
        self.movespeed = 0.1
        # so that the speed doesnt infinitely increase but calms downonce the game resets and comes to the start.



