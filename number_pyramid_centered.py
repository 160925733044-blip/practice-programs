n = 4

for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        print(j, end=" ")

    print()
