s = int(input("S ? "))
t = int(input("T ? "))
n = int(input("N ? "))

for i in range(1,n+1):
    interets = s*t/100
    print(interets)
    s = s + interets

print(s)