count = 0
total = 0

while True:
    num = int(input("Enter a number (enter -1 to stop): "))

    if num == -1:
        break

    total += num
    count += 1

if count == 0:
    print("No numbers entered")
else:
    average = total / count

    print("Count:", count)
    print("Average:", average)
