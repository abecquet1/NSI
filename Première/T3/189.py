def nb_indefinis(table):
    nb = 0
    for e in table:
        for att in e:
            if e[att] is None:
                nb+=1
    return nb

def nb_incompletes(table):
    nb = 0
    for e in table:
        for att in e:
            if e[att] is None:
                nb+=1
                break
    return nb 


table = [
    {"a":0, "b":1},
    {"a":None, "b":1},
    {"a":None, "b":None},
    {"a":0, "b":1},
    {"a":0, "b":None},
    {"a":0, "b":1},
    {"a":0, "b":1},
]

print(nb_indefinis(table))
print(nb_incompletes(table))
