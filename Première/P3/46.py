longueur = 300
largeur = 300

x0 = int(input('x ? '))
y0 = int(input('y ? '))

dx = int(input('dx ? '))
dy = int(input('dy ? '))

assert -longueur <= dx <= longueur and -largeur <= dy <= largeur, "vecteur déplacement trop grand"

if 0 <= x0+dx <= longueur:
    x0 = x0+dx
elif x0+dx > longueur:
    x0 = 2*longueur-x0-dx
else :
    x0 = -x0-dx

if 0 <= y0+dy <= largeur:
    y0 = y0+dy
elif y0+dy > largeur:
    y0 = 2*largeur-y0-dy
else :
    y0 = -y0-dy


