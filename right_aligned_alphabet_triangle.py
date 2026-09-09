n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")

    print()
