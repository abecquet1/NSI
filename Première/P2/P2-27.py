# A l'endroit
n = int(input("Entier :"))
acc = 0
puissance = 10**(n-1)
for i in range(n):
    chiffre = int(input())
    acc = acc + chiffre*puissance
    puissance = puissance // 10
print(acc)

# A l'envers
n = int(input("Entier :"))
acc = 0
puissance = 1
for i in range(n):
    chiffre = int(input())
    acc = acc + chiffre*puissance
    puissance = puissance * 10
print(acc)

