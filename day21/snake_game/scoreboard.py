from turtle import Turtle
AlIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        #self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align= AlIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            with open("highscore.txt", mode="w") as file:
                self.high_score = self.score
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()