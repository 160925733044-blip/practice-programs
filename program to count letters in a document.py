filename = input("Enter the file name: ")

with open(filename, "r") as file:
    text = file.read()

count = 0

for char in text:
    if char.isalpha():
        count += 1

print("Number of letters:", count)
