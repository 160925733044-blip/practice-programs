n = 4

for i in range(n):
    num = 1

    for space in range(n - i - 1):
        print(" ", end=" ")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()
