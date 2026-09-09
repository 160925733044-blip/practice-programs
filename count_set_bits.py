num = int(input("Enter a number: "))

count = 0
while num > 0:
    count += num & 1
    num >>= 1

print("Number of set bits:", count)
