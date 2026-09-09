def triangle(n):
    if n == 0:
        return

    print("*" * n)
    triangle(n - 1)


n = int(input("Enter number of rows: "))

triangle(n)
