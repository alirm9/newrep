smallest = None
largest = None

while True:
    user_input = input("Enter a number (press Enter to quit): ").strip()
    if user_input == "":
        break

    number = float(user_input)

    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

if smallest is not None and largest is not None:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")