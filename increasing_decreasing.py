def print_numbers(n, current):
    if current > n:
        return

    print(current, end=" ")
    print_numbers(n, current + 1)
    print(current, end=" ")


n = int(input("Enter n: "))

print_numbers(n, 1)
