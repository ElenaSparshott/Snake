from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer()


starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_positions:
    new_square = Turtle("square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(position)
    segments.append(new_square)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(start= 2, stop= 0, step= -1,):
        segments[seg_num -1].xcor()
        segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
        


screen.exitonclick()
