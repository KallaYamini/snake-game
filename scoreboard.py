from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")
X_AXIS = 0
Y_AXIS = 265
CHANCE = 3
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("my_file.txt", "r") as data:
                content = data.read()
                self.high_score = int(content) if content else 0
        except FileNotFoundError:
            self.high_score = 0
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(X_AXIS, Y_AXIS)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        with open('my_file.txt','w') as data:
            data.write(str(self.high_score))


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

