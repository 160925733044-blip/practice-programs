def count_vowels(s, index):
    if index == len(s):
        return 0

    if s[index].lower() in "aeiou":
        return 1 + count_vowels(s, index + 1)
    else:
        return count_vowels(s, index + 1)


string = input("Enter a string: ")

print("Number of vowels:", count_vowels(string, 0))
