binary = input("Enter a binary number: ")

decimal = 0
valid = True

for digit in binary:
    if digit != '0' and digit != '1':
        valid = False
        break

    decimal = decimal * 2 + int(digit)

if valid:
    print("Decimal:", decimal)
else:
    print("Invalid binary number")
