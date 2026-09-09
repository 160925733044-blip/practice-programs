def is_palindrome(s, start, end):
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return is_palindrome(s, start + 1, end - 1)


string = input("Enter a string: ")

if is_palindrome(string, 0, len(string) - 1):
    print("Palindrome")
else:
    print("Not a palindrome")
