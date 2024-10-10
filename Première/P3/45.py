xa = float(input("x_A : "))
ya = float(input("y_A : "))
xb = float(input("x_B : "))
yb = float(input("y_B : "))
xc = float(input("x_C : "))
yc = float(input("y_C : "))

xAB = xb-xa
yAB = yb-ya
xAC = xc-xa
yAC = yc-ya

det = xAB*yAC-yAB*xAC

if (xa,ya)==(xb,yb) or (xa,ya)==(xc,yc) or (xb,yb)==(xc,yc) :
    print("Certains points sont confondus...")
else:
    if det == 0 :
        print("A, B et C alignés" )
    else :
        print("A, B et C non alignés" )
    
