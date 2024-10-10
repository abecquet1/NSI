n = int(input("Nombre de notes : "))

s_note = 0 # accumulateur pour sommer les notes
s_coef = 0

for i in range(n):
    note = float(input("Note : "))
    coef = float(input("Coef : "))
    s_note = s_note + note*coef
    s_coef = s_coef + coef


print("Moyenne :", s_note/s_coef)
