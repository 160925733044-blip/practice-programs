num = int(input("Enter a number: "))

sign = -1 if num < 0 else 1
num = abs(num)

reverse = 0

while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

print("Reverse:", sign * reverse)
