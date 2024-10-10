from turtle import *

n = int(input("Nb de lignes :"))
m = int(input("Nb de colonnes :"))

#une possibilité parmi plein d'autres
for i in range(n):
    forward(m*10)
    backward(m*10)
    right(90)
    forward(10)
    left(90)
forward(m*10)


left(90)
for j in range(m):
    forward(n*10)
    backward(n*10)
    left(90)
    forward(10)
    right(90)
