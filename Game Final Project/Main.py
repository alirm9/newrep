# Sustainable Herder - Text Adventure Game
# A game about balancing profit, animal welfare, and nature.

import sys
import time

def print_slow(text):
    """Function to print text slowly for a better text adventure feel."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def show_status(month, money, health, pasture):
    """Display the current farm status."""
    print("\n" + "="*30)
    print(f" Month: {month} / 10")
    print(f" Money: ${money}")
    print(f" Animal Health: {health}%")
    print(f" Pasture Quality: {pasture}%")
    print("="*30 + "\n")

def main():
    # Initial game variables
    month = 1
    money = 1000
    animal_health = 50
    pasture_quality = 50

    print_slow("Welcome to 'The Sustainable Herder'!")
    print_slow("You have inherited a small herd of sheep and a damaged pasture.")
    print_slow("Your goal: Survive 10 months, make money, but keep the animals healthy and save the nature.\n")

    # Main game loop
    while month <= 10:
        show_status(month, money, animal_health, pasture_quality)
        
        print("What do you want to do this month?")
        print("1. Buy food for the herd")
        print("2. Manage the pasture (grazing)")
        print("3. Check farm events")
        print("4. End the month and go to the next")
        print("0. Quit Game")
        
        choice = input("Enter your choice (0-4): ")

        if choice == '1':
            print("\n[ Menu: Food Management ]")
            # Food purchasing logic will go here
            print("1. Cheap industrial food ($50, Health -5%)")
            print("2. Organic feed ($150, Health +10%)")
            input("Press Enter to return to main menu...")

        elif choice == '2':
            print("\n[ Menu: Pasture Management ]")
            # Pasture management logic will go here
            input("Press Enter to return to main menu...")

        elif choice == '3':
            print("\n[ Menu: Farm Events ]")
            # Random events or special actions
            input("Press Enter to return to main menu...")

        elif choice == '4':
            print("\nEnding the month...")
            # Monthly expenses applied at the end of the month
            money -= 50 
            month += 1
            time.sleep(1)

        elif choice == '0':
            print("Thanks for playing! Goodbye.")
            break
        
        else:
            print("Invalid choice! Please enter a number between 0 and 4.")

    # Check game ending conditions
    if month > 10:
        print("\n" + "*"*30)
        print_slow("GAME OVER! Let's see how you did...")
        # Win/Loss logic will be added here later
        print("*"*30)

# Run the program
if __name__ == "__main__":
    main()