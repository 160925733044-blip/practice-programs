num = int(input("Enter a number: "))

if num == 0:
    print("Every non-zero number divides 0")
else:
    num = abs(num)

    print("Divisors:")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
