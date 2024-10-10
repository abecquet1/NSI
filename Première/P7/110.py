# version 1

for i in range(10):
    for j in range(10):
        for k in range(10):
            print(100*i+10*j+k)

# version 2

for i in range(10):
    centaines = i*100
    for j in range(10):
        dizaines = j*10
        for k in range(10):
            print(centaines+dizaines+k)
