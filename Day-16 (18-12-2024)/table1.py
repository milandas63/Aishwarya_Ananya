def padL(n, w):
	r = str(n)
	for i in range(len(r), w):
		r = ' '+r
	return r

start = 2
end = 25

for i in range(start,end+1):
	for j in range(1,11):
		print( padL(i,2), "x", padL(j,2), "=", padL((i*j),3))
	print()

print(); print()

for h in range(start,end+1,5):
	for i in range(1,11):
		for j in range(h,h+5):
			if j>end:
				break
			print(padL(j,2),"x",padL(i,2),"=",padL((i*j),3), end="  ")
		print()
	print()


"""
for(int i=2; i<=10; i++) {
	for(int j=1; j<=10; j++) {
		println(i+" x "+j+" = "+(i*j));
	}
	System.out.println();
}
"""
