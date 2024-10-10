a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if c <= a and c <= b:
    print("Plus petit")
elif c > a and c > b:
    print("Plus grand")
else:
    print("Entre les deux")

