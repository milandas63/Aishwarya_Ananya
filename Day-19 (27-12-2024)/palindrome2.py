line = 9
spaces = 30
for i in range(1,line+1):
    for j in range(0,spaces):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
    spaces = spaces - 1


alpha = 97
spaces = 30

for i in range(1,10):
	for j in range(0,spaces):
		print(' ',end='')
	for j in range(alpha,alpha+i):
		print(chr(j),end='')
	for j in range(alpha+(i-2),alpha-1,-1):
		print(chr(j),end='')
	print()
	spaces = spaces-1
