spaces = 35
stars = 1

for i in range(0,10):
	for j in range(0,spaces):
		print(' ',end='')
	for j in range(0,stars):
		print('*',end='')
	print()
	spaces = spaces-1
	stars = stars+2

print(); print()


spaces = 35
stars = 1

for i in range(0,20):
	for j in range(0,spaces):
		print(' ',end='')
	for j in range(0,stars):
		print('*',end='')
	print()
	if i<9:
		spaces = spaces-1
		stars = stars+2
	else:
		spaces = spaces+1
		stars = stars-2

print(); print()

spaces = 35
for i in range(1,10):
	for j in range(0,spaces):
		print(' ',end='')
	for j in range(1,i+1):
		print(j,end='')
	for j in range(i-1,0,-1):
		print(j,end='')
	print()
	spaces = spaces-1




