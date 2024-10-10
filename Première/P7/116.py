N = 100

t = [True]*N
t[0] = False
t[1] = False

for i in range(N):
    if t[i]:
        for m in range(2*i, N, i): # début : 2*i, fin : N, pas : i
            t[m] = False


for i in range(N):
    if t[i]:
        print(i)