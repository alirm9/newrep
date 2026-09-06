CORRECT_USER = "python"
CORRECT_PASS = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == CORRECT_USER and password == CORRECT_PASS:
        print("Welcome")
        break

    attempts += 1
    if attempts < max_attempts:
        print(
            f"Incorrect credentials. Try again ({max_attempts - attempts} attempts left)."
        )
else:
    print("Access denied")