"""
Write a program to convert all digits in a number to words?
    Example: 12345 = One Two Three Four Five
             03786 = Zero Three Seven Eight Six
             72913 = Seven Two Nine One Three
"""

nlist = ("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine")
digit = input("Enter a 6 digit number: ")
for i in digit:
    n = int(i)
    print(nlist[n],end=' ')
