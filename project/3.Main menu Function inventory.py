def add_item(inventory):
    item = input("Enter item to add to inventory: ")
    inventory.append(item)
    print(f"'{item}' added to your inventory.")

def show_inventory(inventory):
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Your inventory is empty.")
    else:
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")

def clear_inventory(inventory):
    inventory.clear()
    print("Inventory cleared successfully.")

# Main program loop
inventory = []

while True:
    print("\n--- MAIN MENU ---")
    print("1. Add item to inventory")
    print("2. View inventory")
    print("3. Clear inventory")
    print("4. Exit game")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        add_item(inventory)
    elif choice == "2":
        show_inventory(inventory)
    elif choice == "3":
        clear_inventory(inventory)
    elif choice == "4":
        print("Exiting game. Goodbye!")
        break
    else:
        print("Invalid option, please try again.")