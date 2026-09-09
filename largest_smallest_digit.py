num = int(input("Enter a number: "))

num = abs(num)

if num == 0:
    largest = 0
    smallest = 0
else:
    largest = 0
    smallest = 9

    while num > 0:
        digit = num % 10

        if digit > largest:
            largest = digit

        if digit < smallest:
            smallest = digit

        num //= 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)
