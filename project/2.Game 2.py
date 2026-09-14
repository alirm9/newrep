def main():
    age = int(input("Enter your age: "))

    if age < 12:
        print("You are a minor. The program will now shut down.")
        return

    print("Welcome to the game!")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. explore  - Explore the local area")
        print("2. status   - View your character stats")
        print("3. inventory- Check your current items")
        print("4. lopeta   - Exit the game")
        print("-----------------")

        ## until the user enters a valid command we will wait for new lesseons Mr. Kirpal 

        command = input("Enter command: ").strip().lower()

        if command == "lopeta":
            print("Goodbye! Thanks for playing.")
            break
        elif command == "explore":
            print(
                "\nYou venture into the misty forest and spot a glowing shrine!"
            )
        elif command == "status":
            print(
                "\nCharacter Stats: Level 1 Adventurer | Health: 100/100 | Gold: 25"
            )
        elif command == "inventory":
            print("\nInventory: [Wooden Sword], [Health Potion], [Old Map]")
        else:
            print("\nUnknown command. Please choose an option from the menu.")


if __name__ == "__main__":
    main()