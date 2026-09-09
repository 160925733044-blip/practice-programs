a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

while b != 0:
    a, b = b, a % b

print("GCD:", a)
