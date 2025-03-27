from turtle import Turtle, Screen

NORTH_EAST = 45
NORTH_WEST = 135
SOUTH_EAST = 315
SOUTH_WEST = 225


class Ball(Turtle):
    def __init__(self, screen: Screen):
        super().__init__()
        self.shape("circle")
        self.color("lime")
        self.penup()
        self.setheading(NORTH_WEST)
        self.speed("fastest")
        self.screen = screen
        self.hits = 1

    def move(self):
        self.forward(20)

    def hit_wall(self) -> bool:
        wall_line = self.screen.window_height() / 2 - 20
        return wall_line <= self.ycor() or self.ycor() <= -1 * wall_line

    def hit_player(self, player1, player2):
        if self.heading() == NORTH_EAST or self.heading() == SOUTH_EAST:
            if player2.xcor() <= self.xcor() + 40 and player2.ycor() - 40 <= self.ycor() <= player2.ycor() + 40:
                return True
        elif self.heading() == NORTH_WEST or self.heading() == SOUTH_WEST:
            if player1.xcor() >= self.xcor() - 40 and player1.ycor() - 40 <= self.ycor() <= player1.ycor() + 40:
                return True

        return False

    def decide_orientation(self, player1, player2):
        if self.hit_wall():
            self.hits += 1
            if self.heading() == NORTH_WEST:
                self.setheading(SOUTH_WEST)
            elif self.heading() == NORTH_EAST:
                self.setheading(SOUTH_EAST)
            elif self.heading() == SOUTH_WEST:
                self.setheading(NORTH_WEST)
            elif self.heading() == SOUTH_EAST:
                self.setheading(NORTH_EAST)

        if self.hit_player(player1, player2):
            if self.heading() == NORTH_EAST:
                self.setheading(NORTH_WEST)
            elif self.heading() == SOUTH_EAST:
                self.setheading(SOUTH_WEST)
            elif self.heading() == NORTH_WEST:
                self.setheading(NORTH_EAST)
            else:
                self.setheading(SOUTH_EAST)

    def is_goal(self):
        goal_line = self.screen.window_width() / 2
        return self.xcor() <= -1 * goal_line or self.xcor() >= goal_line

    def get_hits(self):
        return self.hits

    def set_hits(self, hits):
        self.hits = hits

    def reset(self):
        self.goto(0,0)
