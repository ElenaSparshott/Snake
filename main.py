from operator import ne
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
    time.sleep(1)
    for seg in segments:
        seg.forward(5)
        


screen.exitonclick()
