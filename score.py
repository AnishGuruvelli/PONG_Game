from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")

class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 250)
        self.write(f"Score: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f"Score: {self.r_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Score: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f"Score: {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
