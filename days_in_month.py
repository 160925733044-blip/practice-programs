month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid month")
elif month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Number of days: 29")
    else:
        print("Number of days: 28")
elif month in [4, 6, 9, 11]:
    print("Number of days: 30")
else:
    print("Number of days: 31")
