base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

if exponent >= 0:
    for i in range(exponent):
        result *= base

    print("Result:", result)
else:
    for i in range(-exponent):
        result *= base

    print("Result:", 1 / result)
