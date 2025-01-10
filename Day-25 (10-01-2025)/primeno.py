start = 1000
end = 3000
count = 0

for i in range(start, end+1):
    yesno = True;
    for j in range(2,i):
        if i%j==0:
            yesno = False
            break;
    if yesno==True:
        print(i, end=' ')
        count = count+1
        if count>=15:
           print()
           count = 0
