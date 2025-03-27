import math
import time
from turtle import Screen

from ball import Ball
from player import Player

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player1, player2 = Player("left", screen), Player("right", screen)
screen.onkey(fun=player2.up, key="Up")
screen.onkey(fun=player2.down, key="Down")
screen.onkey(fun=player1.up, key="w")
screen.onkey(fun=player1.down, key="s")

ball = Ball(screen)
should_continue = True
while should_continue:
    ball.move()
    ball.decide_orientation(player1, player2)
    if ball.is_goal():
        if ball.xcor() < 0:
            player1.scored()
        else:
            player2.scored()
        ball.set_hits(1)
        ball.reset()

        if player1.get_score() == 5 or player2.get_score() == 5:
            should_continue = False

    screen.update()
    time.sleep(0.05 / math.ceil(ball.get_hits() / 5))

screen.exitonclick()
