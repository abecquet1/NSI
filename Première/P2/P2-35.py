n = int(input("Indice du terme ?"))

a = 0 #a va stocker F_n
b = 1 #b va stocker F_n+1

for i in range(n):
    #on passe de (a,b) = (F_i, F_i+1) à (a,b) = (F_i+1, F_i+2)
    c = a+b
    a = b
    b = c

print(a)
#après le dernier passage (i = n-1) on a a = F_n et b = F_n+1
