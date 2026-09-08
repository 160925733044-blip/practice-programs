x = int(input("enter a number:"))
y = int(input("enter a number:"))

print("Before swapping:", x, y)

# Swapping using arithmetic operations
x = x + y
y = x - y
x = x - y

print("After swapping:", x, y)
