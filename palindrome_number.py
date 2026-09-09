num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
