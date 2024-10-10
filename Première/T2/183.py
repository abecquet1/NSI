import csv

# Q1

def guillemets(s):
    return s.replace('"', "'")

print(guillemets('"Coucou", dit-il.'))
print()

# Q2

def compare_cles(d,l):
    return set(d) == set(l)

print(compare_cles({"nom" : "toto", "age":7}, ["nom", "age"]))
print(compare_cles({"nom" : "toto", "age":7}, ["nom"]))
print(compare_cles({"nom" : "toto", "age":7}, ["nom", "age", "ville"]))
print()

# Q3

def affiche_champs(v, dernier):
    vg = '"' + guillemets(str(v)) + '"'
    print(v, end = '')
    if dernier:
        print()
    else:
        print(",", end = "")

affiche_champs("hello", True)
affiche_champs("la réponse est ", False)
print("42")
print()

# Q4

def affiche_csv(t):
    cles = list(t[0])
    for k in cles:
        dernier = (k==cles[-1])
        affiche_champs(k, dernier)
    for e in t:
        if compare_cles(e, cles):
            for k in cles:
                dernier = (k==cles[-1])
                affiche_champs(e[k], dernier)


f = open("exemple.csv", "r")
table = list(csv.DictReader(f))
f.close()

affiche_csv(table)
