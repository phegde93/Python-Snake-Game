from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(height=600, width=600)
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
is_on = True
number_food = 0

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # Detecting collision with Wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or \
            snake.segments[0].ycor() < -290:
        is_on = False
        score_board.game_over()

    # Detecting the Collision
    if snake.segments[0].distance(food) < 15:
        food.refresh_position()
        snake.extend_segment()
        number_food += 1
        score_board.score_tracking(number_food)

    # Detecting Collision with Tail
    for seg in snake.segments:
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10:
            is_on = False
            score_board.game_over()




screen.exitonclick()
