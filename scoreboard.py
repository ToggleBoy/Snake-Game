from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def increase_score(self):

        self.goto(0, 280)
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):

        self.clear()
        self.write(f"Score : {self.score}\tHigh Score: {self.high_score}", align="center", font=('Arial', 12, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #
    #     self.goto(0, 0)
    #     self.write("Game Over.", True, align="center", font=('Arial', 24, 'normal'))
