n = int(input("Côté ? "))

print()
print("Figure 1")
for i in range(n):
    for j in range(i+1):
        print("#", end = "")
    print()


print()
print("Figure 2")
for i in range(n):
    for j in range(n-i):
        print("#", end = "")
    print()

print()
print("Figure 3")
for i in range(n):
    for j in range(i):
        print(".", end = "")
    for j in range(n-i):
        print("#", end = "")
    print()


print()
print("Figure 4")
for j in range(n):
    print("#", end = "")
print()
for i in range(n-2):
    print("#", end = "")
    for j in range(n-2):
        print(".", end = "")
    print("#", end = "")
    print()
for j in range(n):
    print("#", end = "")
print()



