from turtle import *
from math import sin, pi

n = int(input("Nombre de côtés :"))
speed(0)

### flocon ###
for i in range(n):
    forward(200)
    backward(200)
    left(360/n)

#je vais au bon endroit
up()
forward(200)
left (90+180/n)
down()

### hexagone ###
l = 400*sin(pi/n)
for i in range(n):
    forward(l)
    left (360/n)

### il faut faire un peu de géométrie pour comprendre les angles utilisés ici
### sin(pi/n) vient de l'angle 180/n converti en radian (*pi/180)
    
