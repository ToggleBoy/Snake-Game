from turtle import Turtle
position = [(0, 0), (0, -20), (0, -40)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.my_snake = []
        self.snakes()
        self.head = self.my_snake[0]

    def snakes(self):

        for i in position:
            self.add_snake(i)

    def add_snake(self, i):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.setposition(i)
        self.my_snake.append(tim)

    def extend(self):
        self.add_snake(self.my_snake[-1].position())

    def move(self):
        for snakes_numbers in range(len(self.my_snake) - 1, 0, -1):
            # using range to move the snake to front snake position
            new_x = self.my_snake[snakes_numbers - 1].xcor()             # taking the x-axis and storing
            new_y = self.my_snake[snakes_numbers - 1].ycor()             # taking the y-axis and storing
            self.my_snake[snakes_numbers].goto(new_x, new_y)             # updating the value of the snake
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:                 # heading function is to see which direction the snake goes
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.my_snake:
            seg.goto(1000,1000)
        self.my_snake.clear()
        self.snakes()
        self.head = self.my_snake[0]

