num = int(input("Enter a number: "))

num = abs(num)
sum = 0

while num > 0:
    sum += num % 10
    num //= 10

print("Sum of digits:", sum)
