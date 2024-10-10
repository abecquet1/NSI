from turtle import *

speed(1)
#deplacement
up()
goto(-200,0)
x, y = -200, 0
down()

#les deux triangles
begin_fill()
goto(x+50, y+50)
goto(x+25, y-25)
goto(x-50, y+50)
goto(x-25, y-25)
goto(x, y)
end_fill()


#deplacement
up()
goto(0,0)
down()


#radioactif
begin_fill()
forward(50)
left(120)
forward(50)
left(120)
forward(100)
left(120)
forward(50)
left(120)
forward(100)
left(120)
forward(50)
left(120)
end_fill()



#deplacement
up()
goto(200,0)
down()

#triforce
begin_fill()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
end_fill()
forward(50)
left(60)
fillcolor("white")
begin_fill()
forward(50)
left(120)
forward(50)
left(120)
forward(50)
left(60)
end_fill()
fillcolor("black")


#deplacement
up()
goto(0,-200)
down()

#yin yang
circle(50, 180)
begin_fill()
circle(50, 180)
circle(25, -180)
left(180)
circle(25, 180)
end_fill()
left(90)
forward(25)
color("white")
dot(10)
up()
forward(50)
down()
color("black")
dot(10)


