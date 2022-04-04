from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn turtle animation on/off and set delay for update drawings
screen.bgcolor("black")
screen.title("My Snake Game ")

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()  # Updating the tracer value here / refresh the screen <--
    time.sleep(0.1)  # Setting the time to delay the result for given time ---^
    snake.move()

    if snake.head.distance(food) < 15:
        # snake head is near the food to find that we use distance function
        # from the class turtle and used compare the distance from food to snake
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # detect head collision with body
    # we need to loop to the segments in the snake
    for segments in snake.my_snake[1:]:         # slicing method 
        # if segments == snake.head:
        #     pass
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
