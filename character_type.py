ch = input("Enter a character: ")

if len(ch) != 1:
    print("Enter only one character")
elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("Alphabet")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special character")
