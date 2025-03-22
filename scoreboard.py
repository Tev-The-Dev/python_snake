from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_new_high_score()
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def calculate_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            stored_score = int(file.read())
            return stored_score

    def set_new_high_score(self):
        with open("data.txt", "w") as file:
            new_high_score = str(self.high_score)
            file.write(new_high_score)
