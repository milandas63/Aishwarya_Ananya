# Draw a hollow triangle using reverse palindrome number?

x = 1
spaces = 30
for i in range(1,10):
    for j in range(0,spaces):
        print(" ",end="")
    for j in range(1,x+1):
        if j==1 or j==x or i==9: 
            print("*",end="")
        else:
            print(".",end="")
    print()
    spaces = spaces - 1
    x = x + 2
