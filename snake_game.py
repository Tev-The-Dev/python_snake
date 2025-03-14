from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_array = []

for s in range(0,3):
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake_array.append(snake)

x_position = 0
for snake in snake_array:
    snake.goto(x_position, 0)
    x_position-=20
















screen.exitonclick()