def triangle(n, row=1):
    if row > n:
        return

    print(" " * (row - 1) + "*" * (n - row + 1))
    triangle(n, row + 1)


n = int(input("Enter number of rows: "))

triangle(n)
