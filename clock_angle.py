hour = int(input("Enter hour (1-12): "))
minute = int(input("Enter minute (0-59): "))

if hour < 1 or hour > 12 or minute < 0 or minute > 59:
    print("Invalid time")
else:
    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6

    difference = abs(hour_angle - minute_angle)

    if difference > 180:
        difference = 360 - difference

    print("Smaller angle:", difference, "degrees")
