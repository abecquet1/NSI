a = int(input("Donner un entier : "))
b = int(input("Donner un entier : "))
c = int(input("Donner un entier : "))


# on procède par échange de valeurs entre les variables a, b et c

if a > b:
    tmp = a
    a = b
    b = tmp

# on a forcé a <= b

if b > c:
    tmp = b
    b = c
    c = tmp

# on a forcé b <= c et que a <= c

if a > b:
    tmp = a
    a = b
    b = tmp

# on a forcé a <= b <= c

print(a, b, c)

