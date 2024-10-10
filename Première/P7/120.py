from turtle import *

def carre(cote, b):
    if b: begin_fill()
    for i in range(4):
        forward(cote)
        left(90)
    if b: end_fill()

def damier(n, cote = 10):
    premiere_case_blanche = True
    for i in range(n):

        b = premiere_case_blanche
        for j in range(n):
            carre(cote, b)
            forward(cote)
            b = not(b)

        backward(cote*n)
        left(90)
        forward(cote)
        right(90)
        premiere_case_blanche = not(premiere_case_blanche)

damier(5)

