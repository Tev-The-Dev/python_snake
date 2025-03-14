from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20, 0), (-40, 0)]
snake_array = []

for s in starting_positions:
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(s)
    snake_array.append(snake)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(snake_array)-1,0,-1):
        new_x = snake_array[seg -1].xcor()
        new_y = snake_array[seg - 1].ycor()
        snake_array[seg].goto(new_x, new_y)
    snake_array[0].forward(20)





screen.exitonclick()