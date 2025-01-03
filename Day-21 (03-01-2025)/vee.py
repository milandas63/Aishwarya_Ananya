"""
            1               1
            12             21
            123           321
            1234         4321
            12345       54321
            123456     654321
            1234567   7654321
            12345678 87654321
            12345678987654321
"""

spaces = 17
for l in range(1,11):
    for s in range(0,20):
        print(" ", end="")
    for t in range(1,l):
        print(t, end="")
    for s in range(0,spaces):
        print(" ", end="")
    if l<10:
        k = l-1
    else:
        k = l-2
    for t in range(k,0,-1):
        print(t, end="")
    spaces = spaces - 2
    print()



spaces = 15
for l in range(1,10):
    for s in range(0,20):
        print(" ", end="")
    for t in range(1,l+1):
        print(t, end="")
    for s in range(0,spaces):
        print(" ", end="")
    k = l
    if l==9:
        k = 8
    for t in range(k,0,-1):
        print(t, end="")
    spaces = spaces - 2
    print()


