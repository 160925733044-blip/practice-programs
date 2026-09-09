num = int(input("Enter a number: "))

if num <= 0:
    print("Not a perfect number")
else:
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        print("Perfect number")
    else:
        print("Not a perfect number")
