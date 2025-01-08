"""
    Flip/Invert/Toggle the case of all characters in a given String?

    Original:   Quick Brown Fox Jumps Over The Lazy Dog
    Invert:     qUICK bROWN fOX jUMPS oVER tHE lAZY dOG
"""

original_text = "Quick Brown Fox Jumps Over The Lazy Dog"
for i in original_text:
    code = ord(i)
    if code>=65 and code<=90:
        code = code+32
        print(chr(code),end="")
    elif code>=97 and code<=122:
        code = code-32
        print(chr(code),end="")
    else:
        print(i,end="")
print()
