num = int(input("Enter a number: "))

original = num
num = abs(num)

digits = len(str(num))
total = 0

temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
