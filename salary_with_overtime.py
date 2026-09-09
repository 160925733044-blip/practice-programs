hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    salary = hours * rate
else:
    regular_salary = 40 * rate
    overtime_hours = hours - 40
    overtime_salary = overtime_hours * rate * 1.5
    salary = regular_salary + overtime_salary

print("Total salary:", salary)
