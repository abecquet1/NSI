from turtle import *
R = 300 #rayon de l'arc
b = 20  #épaisseur desz bandes
speed(0)#pour aller plus vite

r = R
fillcolor("red")
begin_fill()
backward(r)
forward(2*r)
left(90)
circle(r, 180)
left(90)
forward(r)
end_fill()

r = r-b
fillcolor("orange")
begin_fill()
backward(r)
forward(2*r)
left(90)
circle(r, 180)
left(90)
forward(r)
end_fill()

r = r-b
fillcolor("yellow")
begin_fill()
backward(r)
forward(2*r)
left(90)
circle(r, 180)
left(90)
forward(r)
end_fill()

r = r-b
fillcolor("green")
begin_fill()
backward(r)
forward(2*r)
left(90)
circle(r, 180)
left(90)
forward(r)
end_fill()

r = r-b
fillcolor("blue")
begin_fill()
backward(r)
forward(2*r)
left(90)
circle(r, 180)
left(90)
forward(r)
end_fill()

r = r-b
fillcolor("darkviolet")
begin_fill()
backward(r)
forward(2*r)
left(90)
circle(r, 180)
left(90)
forward(r)
end_fill()

r = r-b
fillcolor("magenta")
begin_fill()
backward(r)
forward(2*r)
left(90)
circle(r, 180)
left(90)
forward(r)
end_fill()

r = r-b
fillcolor("white")
begin_fill()
backward(r)
forward(2*r)
left(90)
circle(r, 180)
left(90)
forward(r)
end_fill()

color("white")
backward(r)
forward(2*r)

