num = int(input("Enter a number: "))

num = abs(num)
product = 1

if num == 0:
    product = 0
else:
    while num > 0:
        product *= num % 10
        num //= 10

print("Product of digits:", product)
