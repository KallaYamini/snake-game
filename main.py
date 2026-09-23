from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()

screen.setup(width=600, height=600, startx=0, starty=0)
screen.title("Snake Game...")
screen.tracer(0)

game_on = True
score = 0

def stop_game():
    global game_on
    game_on = False

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop_game, "space")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset_score()
            snake.reset_snake()

    for segment in snake.segments[1:]:
        # skip the head itself
        if snake.head.distance(segment) < 10:
            # collision detected
            scoreboard.reset_score()
            snake.reset_snake()

screen.bye()
