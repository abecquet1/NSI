from turtle import *
from math import sqrt

#deplacement
up()
goto(-200,0)
down()

speed(1)

#croix
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()
forward(50)
left(90)
forward(50)
color("white")
width(5)
forward(25)
backward(25)
left(90)
forward(25)
backward(25)
left(90)
forward(25)
backward(25)
left(90)
forward(25)
backward(25)
left(90)


#deplacement
up()
goto(0,0)
color("black")
down()

#???
dot(5)
up()
forward(10)
left(180)
down()
circle(50, -45)
left(180)
circle(25, 180+45)

#deplacement
up()
goto(100,0)
down()
left(90)

#unity
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
left(30)
width(1)
forward(2*100/3*sqrt(3)/2)
left(120)
backward(2*100/3*sqrt(3)/2)
forward(2*100/3*sqrt(3)/2)
left(120)
backward(2*100/3*sqrt(3)/2)
forward(2*100/3*sqrt(3)/2)







