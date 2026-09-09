num = int(input("Enter a 3-digit number: "))

if num < 100 or num > 999:
    print("Please enter a 3-digit number")
else:
    original = num

    a = num // 100
    b = (num // 10) % 10
    c = num % 10

    sum_cubes = a ** 3 + b ** 3 + c ** 3

    if sum_cubes == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
