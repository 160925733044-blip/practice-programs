def triangle(n):
    if n == 0:
        return

    triangle(n - 1)
    print("*" * n)


n = int(input("Enter number of rows: "))

triangle(n)
