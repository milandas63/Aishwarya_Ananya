text = "This is an English sentence containing several word"
vowels = "AEIOUaeiou"

count = 0
for i in text:
    for j in vowels:
        if i==j:
            count = count+1
            break

print("Total vowels = ",count)
