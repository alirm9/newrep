airports = {}

while True:
    print("\nOptions:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print(f"Airport {name} ({icao}) added.")
    elif choice == "2":
        icao = input("Enter ICAO code: ").upper()
        if icao in airports:
            print(f"Airport name: {airports[icao]}")
        else:
            print("Airport not found.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")