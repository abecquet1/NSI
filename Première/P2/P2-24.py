n = int(input("Entrer un entier n : "))

acc = 0

for i in range(1,n+1):
    acc = acc+i

print("Somme des n premiers entiers :", acc)
print("n(n+1)/2 :", n*(n+1)//2)
