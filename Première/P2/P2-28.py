n = int(input("Entier : "))
k = int(input("Nb de chifrres à afficher : "))
quotient = n

for i in range(k):
    reste = quotient % 10
    quotient = quotient // 10
    print(reste)
print()
