from turtle import Turtle, Screen
import random

tm = Turtle()

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Black']
gradus = [0, 90, 180, 270]
tm.pensize(10)
for i in range(500):
   tm.color(random.choice(colors))
   tm.setheading(random.choice(gradus))
   tm.forward(40)