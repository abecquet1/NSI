from turtle import *

"""
proportions : le drapeau français est au format 2:3
c'est à dire que pour une largeur de 300, il aura une hauteur de 200
on peut donc dessiner les trois bandes d couleurs aux dimensions 100*200
"""

up()
goto(-100, 0)
down()

#bleu
fillcolor("blue")
begin_fill()
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
end_fill()

#blanc
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)


#rouge
fillcolor("red")
begin_fill()
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
end_fill()


up()
goto(-100, -300)
down()

"""
drapeau belge : format 13:15 en noir jaune rouge
"""

#noir
fillcolor("black")
begin_fill()
forward(100)
left(90)
forward(260)
left(90)
forward(100)
left(90)
forward(260)
left(90)
forward(100)
end_fill()

#jaune
fillcolor("yellow")
begin_fill()
forward(100)
left(90)
forward(260)
left(90)
forward(100)
left(90)
forward(260)
left(90)
forward(100)
end_fill()

#rouge
fillcolor("red")
begin_fill()
forward(100)
left(90)
forward(260)
left(90)
forward(100)
left(90)
forward(260)
left(90)
forward(100)
end_fill()








