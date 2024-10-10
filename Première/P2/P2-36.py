from turtle import *

n = int(input("Valeur de n (n=7 pour l'exemple de l'ennoncé) ?"))

a = 0 
b = 1 

for i in range(n):
    #meme algo que 35 pour le calcul des termes avec le tracé du cercle en plus
    circle(a*20,90)
    c = a+b
    a = b
    b = c

