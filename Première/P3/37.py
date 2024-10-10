n = int(input("Entrer un entier pour connaître ses diviseurs :"))
for d in range(1,n+1):
    if n%d==0:
        print(d, "divise", n)
