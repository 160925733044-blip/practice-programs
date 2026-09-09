hour = int(input("Enter hour (0-23): "))

if hour < 0 or hour > 23:
    print("Invalid hour")
elif hour < 12:
    print("Good Morning")
elif hour < 17:
    print("Good Afternoon")
elif hour < 21:
    print("Good Evening")
else:
    print("Good Night")
