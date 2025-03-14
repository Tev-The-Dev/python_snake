from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.snake_array = []
        self.create_snake()

    def create_snake(self):
        # Creates the snake
        for s in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(s)
            self.snake_array.append(snake)

    def move(self):
        for seg in range(len(self.snake_array) - 1, 0, -1):
            new_x = self.snake_array[seg - 1].xcor()
            new_y = self.snake_array[seg - 1].ycor()
            self.snake_array[seg].goto(new_x, new_y)
        self.snake_array[0].forward(MOVE_DISTANCE)
    def up(self):
        self.snake_array[0].setheading(90)
    def down(self):
        self.snake_array[0].setheading(270)
    def left(self):
        self.snake_array[0].setheading(180)
    def right(self):
        self.snake_array[0].setheading(0)