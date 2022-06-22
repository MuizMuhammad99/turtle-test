import random
from turtle import Turtle, Screen

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270,360]


turtle = Turtle()
#turtle.pensize(15)
#for i in range(200):
 #   turtle.color(random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
  #  turtle.setheading(random.choice(directions))
   # turtle.forward(50)


x = 50
turtle.speed(0)
#for i in range (50):
    #turtle.color(random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
   # degrees = 360/x
  #  turtle.right(degrees)
 #   turtle.circle(100)

turtle.speed("fastest")
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = Screen()
screen.exitonclick()