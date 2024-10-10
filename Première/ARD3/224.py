def printASCII(s):
    for c in s:
        print(hex(ord(c))[2:], end = " ")
    print()

printASCII("bonjour tout le monde!")
printASCII("programmer en\nPython")
