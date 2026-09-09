def triangle(n, row=1):
    if row > n:
        return

    print(" " * (n - row) + "*" * row)
    triangle(n, row + 1)


n = int(input("Enter number of rows: "))

triangle(n)
