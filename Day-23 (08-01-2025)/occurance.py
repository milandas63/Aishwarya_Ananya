"""
    Count and report the number of occurrences of each character in a given string?

    Hello World    Students Allowed       Holocaust
       D = 1           A - 1                A - 1
       E - 1           D - 2                C - 1
       H - 1           E - 2                H - 1
       L - 3           L - 1                L - 1
       O - 2           N - 1                O - 2
       R - 1           O - 1                S - 1
       W - 1           S - 2                T - 1
                       T - 2                U - 1
                       U - 1
                       W - 1
"""

text = "Students Allowed"
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in text:
    code = ord(i)
    if code>=65 and code<=90:
        code = code-65
        count[code] = count[code]+1
    elif code>=97 and code<=122:
        code = code-97
        count[code] = count[code]+1

for i in range(0,len(count)):
    if count[i]>0:
        print(chr(i+65)," = ",count[i])
