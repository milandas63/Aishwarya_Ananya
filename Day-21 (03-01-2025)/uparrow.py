"""
            12345678987654321
            12345678 87654321
            1234567   7654321
            123456     654321
            12345       54321
            1234         4321
            123           321
            12             21
            1               1

"""
spaces = 0
for l in range(9,0,-1):
    for s in range(0,20):
        print(' ',end='')
    for t in range(1,l+1):
        print(t,end='')
    for s in range(1,spaces):
        print(' ',end='')
    k = l
    if l==9:
        k = l-1
    for t in range(k,0,-1):
        print(t,end='')
    print()
    spaces = spaces+2
