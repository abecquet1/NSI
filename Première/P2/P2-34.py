from turtle import *
from math import cos,pi

#j'ai choisi de pouvoir paramétrer la hauteur de la figure et l'angle formé entre les traits
#cela amène à devoir faire un peu de géométrie...
nb_epaisseur = 5
hauteur = 500
angle = 30

right(90)
for epaisseur in range(1,nb_epaisseur+1):
    width(epaisseur)
    forward(hauteur/nb_epaisseur)
up()
goto(-hauteur/4,0)
right(angle)
down()
for epaisseur in range(1,nb_epaisseur+1):
    width(epaisseur)
    forward(hauteur/cos(angle*pi/180)/nb_epaisseur)
up()
goto(hauteur/4,0)
left(angle*2)
down()   
for epaisseur in range(1,nb_epaisseur+1):
    width(epaisseur)
    forward(hauteur/cos(angle*pi/180)/nb_epaisseur)
