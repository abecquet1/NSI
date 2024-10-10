from turtle import *

n = int(input("Combien de nuance de gris ?"))

if n == 50:
    raise ValueError("Tout sauf ça svp.")

for i in range(n):
    fillcolor(i/(n-1),i/(n-1),i/(n-1))
    begin_fill()
    forward(100/n)
    right(90)
    forward(50)
    right(90)
    forward(100/n)
    right(90)
    forward(50)
    right(90)
    end_fill()
    forward(100/n)


