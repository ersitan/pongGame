from turtle import Turtle, Screen
from score import Score

EDGE = 380
MOVE_DISTANCE = 40
SCORE_PLACE = 60


class Player(Turtle):
    def __init__(self, direction, screen: Screen):
        super().__init__()
        self.screen = screen
        self.player_score = 0
        self.direction = direction.lower()
        self.shape("square")
        self.resizemode("user")
        self.turtlesize(5, 1, 0)
        self.penup()
        self.color("white")
        self.score = Score(screen)

        self.initialize()

    def initialize(self):
        score_x_cor = -1 * SCORE_PLACE
        direction = EDGE
        if self.direction == "left":
            direction = -1 * EDGE
            score_x_cor = SCORE_PLACE

        self.teleport(direction, 0)
        self.score.initialize(score_x_cor)

    def up(self):
        self.teleport(self.xcor(), self.ycor() + MOVE_DISTANCE)
        return 0

    def down(self):
        self.teleport(self.xcor(), self.ycor() - MOVE_DISTANCE)
        return 0

    def scored(self):
        self.score.scored()

    def get_score(self):
        return self.score.get_score()
