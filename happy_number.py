num = int(input("Enter a number: "))

seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** 2
        num //= 10

    num = total

if num == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
