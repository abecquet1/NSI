### Exercice 69 ###
def ex69():
    pda = [123,456,789,321,654,987]
    age_min = int(input())
    age_max = int(input())
    somme = 0
    for i in range(age_min, age_max):
        if 0 <= i < len(pda):
            somme = somme + pda[i]
    return somme


### Exercice 70 ###
def occurences(v, t):
    compteur = 0
    for i in range(len(t)):
        if v == t[i]:
            compteur += 1
    return compteur


### Exercice 71 ###
from random import *
def ex71():
    t = [0]*100
    for i in range(len(t)):
        t[i] = randint(1,1000)
    print(t)


### Exercice 72 ###
from random import *
def ex72():
    #création du tableau
    t = [0]*100
    for i in range(len(t)):
        t[i] = randint(1,1000)

    #recherche du max
    maximum = 1
    for i in range(len(t)):
        if t[i] > maximum:
            maximum = t[i]

    print(t)
    print("max :", maximum)



### Exercice 73 ###
from random import *
#On va créer un tableau qui comptera pour chaque indice entre 0 et 10 (le 0 ne servant à rien), le nombre de fois que l'indice est tiré
def ex73():
    tab_compteur = [0]*11
    for i in range(1000):
        j = randint(1,10)
        tab_compteur[j] += 1
    return tab_compteur



### Exercice 74 ###
def ex74():
    fibo = [0]*30
    fibo[1] = 1
    for i in range(2,30):
        fibo[i] = fibo[i-1]+fibo[i-2]
    print(fibo)


### Exercice 75 ###
def copie(t):
    res = [0]*len(t)
    for i in range(len(t)):
        res[i] = t[i]
    return res


#il suffit de copier un tableau, de le modifier et de voir si cela a un effet sur l'autre
def ex75():
    t = [1,2,3,4,5]
    u = copie(t)
    t[0] = 12
    u[1] = 42
    print(t)
    print(u)



### Exercice 76 ###
def ajout(v,t):
    n = len(t)
    res = [0]*(n+1)
    for i in range(n):
        res[i] = t[i]
    res[n] = v
    return res


### Exercice 77 ###
def concatenation(t1, t2):
    n = len(t1)
    m = len(t2)
    res = [0]*(n+m)
    for i in range(n):
        res[i] = t1[i]
    for i in range(m):
        res[n+i] = t2[i]
    return res




def concatenation_bis(t1,t2):
    res = copie(t1)
    for i in range(len(t2)):
        res = ajout(t2[i], res)
    return res




### Exercice 78 ###
def tableau_aleatoire(n, a, b):
    t = [0]*n
    for i in range(n):
        t[i] = randint(a,b)
    return t




### Exercice 79 ###
def tableau_croissant(n):
    t = [0]*n
    t[0] = randint(0,10)
    for i in range(1,n):
        t[i] = t[i-1]+randint(0,10)
    return t



### Exercice 80 ###
def echange(t, i, j):
    tmp = t[i]
    t[i] = t[j]
    t[j] = tmp


### Exercice 81 ###
def somme(t):
    res = 0
    for i in range(len(t)):
        res = res + t[i]
    return res




### Exercice 82 ###
def produit(t):
    res = 1
    for i in range(len(t)):
        if t[i]==0:
            return 0
        res = res*t[i]
    return res




### Exercice 83 ###
def miroir(t):
    n = len(t)
    for i in range(n//2):
        echange(t, i, n-1-i)



### Exercice 84 ###
def melange(t):
    n = len(t)
    for i in range(1,n):
        j = randint(0,i)
        echange(t, i, j)


### Exercice 85 ###
def prefixe(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    if n1>n2:
        return False
    for i in range(n1):
        if t1[i]!=t2[i]:
            return False
    return True


### Exercice 86 ###
def suffixe(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    if n1>n2:
        return False
    for i in range(n1):
        if t1[i]!=t2[n2-n1+i]:#faire un schéma pour comprendre l'indice dans t2
            return False
    return True



### Exercice 87 ###
def hamming(t1, t2):
    compteur = 0
    for i in range(len(t1)):
        if t1[i]!=t2[i]:
            compteur = compteur + 1
    return compteur



### Exercice 89 ###
def nb_jours_mois(a,m):
    jours = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if m != 2:
        return jours[m]
    else:
        if (a%4 == 0 and a%100 !=0) or a%400==0:
            return 29
        else :
            return 28



