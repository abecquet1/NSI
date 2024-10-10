"""
on cherche x, y tels que :
y = ax + b
y = cx + d

en particulier, y=y donne :
    ax + b = cx + d
<=> ax - cx = d - b
<=> (a - c)x = d - b
<=> x = (d - b)/(a - c)   si a différent de c

la valeur de x étant connue, on peut retrouver y par le calcul :
y = ax + b
"""

a = int(input("a ? "))
b = int(input("b ? "))
c = int(input("c ? "))
d = int(input("d ? "))

x = (d-b)/(a-c)
y = a*x+b

print("Intersection : (", x, ",", y, ")")
