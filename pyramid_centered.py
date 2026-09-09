def pyramid(n, row=1):
    if row > n:
        return

    spaces = " " * (n - row)
    stars = "*" * (2 * row - 1)

    print(spaces + stars)
    pyramid(n, row + 1)


n = int(input("Enter number of rows: "))

pyramid(n)
