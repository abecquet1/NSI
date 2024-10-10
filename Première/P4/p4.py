from turtle import*

# ex57
def test_pythagore(a,b,c):
    return a**2+b**2==c**2

#ex58
def valeur_absolue(x):
    if x>=0:
        return x
    else:
        return -x

#ex 60
def max2(a,b):
    if a>=b:
        return a
    else:
        return b

#ex 61
def max3(a,b,c):
    return max2(max2(a,b),c)


#ex 62
def puissance(x,k):
    res=1
    for i in range(k):
        res=res*x
    return res

#ex 63
def bissextile(a):
    return (a%4==0 and a%100!=0) or a%400==0


#ex 64
def nb_jours_annee(a):
    if bissextile(a):
        return 366
    else:
        return 365

#ex 65
def nb_jours_mois(a,m):
    if m == 2 :
        if bissextile(a):
            return 29
        else:
            return 28
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m==12 :
        return 31
    else:
        return 30


#ex 66
def nb_jours(j1,m1,a1,j2,m2,a2):

    acc1 = 0
    for a in range(0, a1):
        acc1 = acc1 + nb_jours_annee(a)
    for m in range(1, m1):
        acc1 = acc1 + nb_jours_mois(a1, m)
    acc1 = acc1 + j1

    acc2 = 0
    for a in range(0, a2):
        acc2 = acc2 + nb_jours_annee(a)
    for m in range(1, m2):
        acc2 = acc2 + nb_jours_mois(a2, m)
    acc2 = acc2 + j2

    return acc2-acc1


#ex 67
def ex67():
    a = int(input("Année ? "))
    for m in range(1,13):
        for j in range(1,nb_jours_mois(a,m)+1):
            print(j,'/',m,'/',a)




#ex 68
def triangle(cote):
    begin_fill()
    for i in range(3):
        forward(cote)
        left(120)
    end_fill()

def radio(cote):
    for i in range(3):
        triangle(cote)
        left(120)

def triforce(cote):
    triangle(2*cote)
    forward(cote)
    left(60)
    fillcolor('white')
    triangle(cote)
    fillcolor('black')

def sapin(cote):
    #triangle 1
    triangle(2*cote)
    forward(cote)
    left(90)
    forward(1.1*cote)
    right(90)
    backward(cote/2)
    #triangle 2
    triangle(cote)
    forward(cote/2)
    left(90)
    forward(1.1*cote/2)
    right(90)
    backward(cote/4)
    #triangle 3
    triangle(cote/2)







