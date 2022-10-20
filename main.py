from snake import Snake
from food import Food
from scoreboard import Scoreboard
import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.move()
        scoreboard.update_score()

    # Detect collision with wall
    snake_x = snake.head.xcor()
    snake_y = snake.head.ycor()
    if snake_x > 290 or snake_x < -290 or snake_y > 290 or snake_y < -290:
        # game_is_on = False
        scoreboard.game_over()
        snake.reset()

    # Detect collision with snake
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.game_over()
            snake.reset()































screen.exitonclick()
