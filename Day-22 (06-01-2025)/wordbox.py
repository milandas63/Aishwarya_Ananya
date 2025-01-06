text = "Do not make extravagent expenditure"
text = "Ananya Aishwarya Milan Subhashis Phantom Tarzen"
text = "US UK India Bangladesh Srilanka Pakistan China Australia"
big = 0
word_array = text.split()
for i in word_array:
    if len(i)>big:
        big = len(i)

for i in range(0, (big+4)):
    print("*",end="")
print()

for i in word_array:
    print("* ",i.ljust(big)," *",sep="")

for i in range(0, (big+4)):
    print("*",end="")
print()
print()

for i in range(len(word_array)-1,-1,-1):
    for j in range(len(word_array[i])-1,-1,-1):
        print(word_array[i][j],end="")
    print(" ",end="")
print()
