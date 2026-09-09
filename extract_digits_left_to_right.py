num = int(input("Enter a number: "))

num = abs(num)

divisor = 1
temp = num

while temp >= 10:
    divisor *= 10
    temp //= 10

while divisor > 0:
    digit = num // divisor
    print(digit)
    num %= divisor
    divisor //= 10
