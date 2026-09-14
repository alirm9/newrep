def gallons_to_liters(gallons):
    return gallons * 3.78541

# Main program
while True:
    gallons_input = float(input("Enter volume in gallons (negative value to quit): "))
    if gallons_input < 0:
        print("Program ended.")
        break
    liters = gallons_to_liters(gallons_input)
    print(f"{gallons_input} gallons is equal to {liters:.2f} liters.")