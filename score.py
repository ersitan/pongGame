from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self, screen: Screen):
        super().__init__()
        self.player_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.screen = screen

    def initialize(self, xcor):
        self.goto(xcor, self.screen.window_height()/2 - 60)
        self.write_score()

    def scored(self):
        self.player_score += 1
        if self.player_score < 5:
            self.clear()
        self.write_score()

    def write_score(self):
        self.write(self.player_score, align="center", font=("Arial", 40, "normal"))
        if self.player_score == 5:
            self.goto(0, 0)
            self.write("Game over", align="center", font=("Arial", 40, "normal"))

    def get_score(self):
        return self.player_score
