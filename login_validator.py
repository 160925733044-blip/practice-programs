username = input("Enter username: ")
password = input("Enter password: ")

# Example valid credentials
correct_username = "admin"
correct_password = "12345"

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")
