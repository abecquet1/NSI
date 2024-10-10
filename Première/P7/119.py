
def present(t1, t2, i):
    """t1 se trouve-t-il dans t2 à partir de i ?"""
    if len(t1)>len(t2)-i:
        return False
    for j in range(len(t1)):
        if t1[j] != t2[i+j]:
            return False
    return True

def facteur(t1, t2):
    for i in range(len(t2)):
        if present(t1, t2, i):
            return True
    return False

t1 = [1,2,3]
t2 = [0,1,2,3,4]
t3 = [2,3]
t4 = [0,1,2]
t5 = [1,1,2,2,3,3]

print(facteur([], t1))
print(facteur(t1, t2))
print(facteur(t1, t3))
print(facteur(t1, t4))
print(facteur(t1, t5))
print()

def facteur(t1, t2):
    for i in range(len(t2)):
        j = 0
        while j < len(t1) and i+j < len(t2) and t2[i+j] == t1[j]:
            j = j+1
        if j == len(t1):
            return True
    return False

print(facteur([], t1))
print(facteur(t1, t2))
print(facteur(t1, t3))
print(facteur(t1, t4))
print(facteur(t1, t5))

