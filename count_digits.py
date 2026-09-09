num = int(input("Enter a number: "))

num = abs(num)

if num == 0:
    count = 1
else:
    count = 0

    while num > 0:
        count += 1
        num //= 10

print("Number of digits:", count)
