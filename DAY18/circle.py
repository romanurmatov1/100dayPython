from turtle import Turtle, Screen
import random
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Black']


tm = Turtle()
tm.speed('fastest')

def ds(sog):
   for i in range(int(360 / sog)):
      tm.color(random.choice(colors))
      tm.circle(100)
      tm.setheading(tm.heading()+sog)
ds(5)

screen = Screen()
screen.exitonclick()