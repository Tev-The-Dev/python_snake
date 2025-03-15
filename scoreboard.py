from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)


    def calculate_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

