# Sustainable Herder - Text Adventure Game
# A game about balancing profit, animal welfare, and nature.

import sys
import time
import random  # Added for random events

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
    event_checked = False  # To prevent spamming events in a single month

    print_slow("Welcome to 'The Sustainable Herder'!")
    print_slow("You have inherited a small herd of sheep and a damaged pasture.")
    print_slow("Your goal: Survive 10 months, make money, but keep the animals healthy and save the nature.\n")

    # Main game loop
    while month <= 10:
        show_status(month, money, animal_health, pasture_quality)
        
        print("What do you want to do this month?")
        print("1. Buy food for the herd")
        print("2. Manage the pasture (grazing)")
        print("3. Check farm events (Once per month)")
        print("4. End the month and go to the next")
        print("0. Quit Game")
        
        choice = input("Enter your choice (0-4): ")

        # --- MENU 1: FOOD MANAGEMENT ---
        if choice == '1':
            print("\n[ Menu: Food Management ]")
            print("1. Cheap industrial food ($50, Health -5%)")
            print("2. Organic feed ($150, Health +10%)")
            print("0. Cancel and return")
            
            food_choice = input("Select an option (0-2): ")
            
            if food_choice == '1':
                if money >= 50:
                    money -= 50
                    animal_health -= 5
                    print("Result: You bought cheap industrial food. The animals don't look very happy.")
                else:
                    print("Result: Not enough money!")
            
            elif food_choice == '2':
                if money >= 150:
                    money -= 150
                    animal_health += 10
                    print("Result: You bought organic feed. The herd looks healthy and energetic!")
                else:
                    print("Result: Not enough money!")
            
            elif food_choice == '0':
                print("Returning to main menu...")
            else:
                print("Invalid choice.")

            # Keep health within limits
            if animal_health > 100: animal_health = 100
            elif animal_health < 0: animal_health = 0

            input("\nPress Enter to return to main menu...")

        # --- MENU 2: PASTURE MANAGEMENT ---
        elif choice == '2':
            print("\n[ Menu: Pasture Management ]")
            print("1. Free Grazing (Cost: $0, Pasture Quality -15%)")
            print("2. Rotational Grazing (Cost: $100, Pasture Quality +10%)")
            print("0. Cancel and return")
            
            pasture_choice = input("Select an option (0-2): ")
            
            if pasture_choice == '1':
                pasture_quality -= 15
                print("Result: You let the herd roam freely. The land is overgrazed and heavily damaged.")
            
            elif pasture_choice == '2':
                if money >= 100:
                    money -= 100
                    pasture_quality += 10
                    print("Result: You set up fences for rotational grazing. The pasture has time to recover!")
                else:
                    print("Result: Not enough money for fencing!")
            
            elif pasture_choice == '0':
                print("Returning to main menu...")
            else:
                print("Invalid choice.")

            # Keep pasture quality within limits
            if pasture_quality > 100: pasture_quality = 100
            elif pasture_quality < 0: pasture_quality = 0

            input("\nPress Enter to return to main menu...")

        # --- MENU 3: FARM EVENTS (RANDOM) ---
        elif choice == '3':
            print("\n[ Menu: Farm Events ]")
            if event_checked:
                print("You have already checked for events this month. Wait until next month!")
            else:
                event_checked = True
                event_roll = random.randint(1, 3)
                
                if event_roll == 1:
                    print("Event: A rainy week! The pasture grew beautifully. (Pasture Quality +15%)")
                    pasture_quality += 15
                elif event_roll == 2:
                    print("Event: A local fair! You sold some extra wool. (Money +$100)")
                    money += 100
                elif event_roll == 3:
                    print("Event: Wolf sighting near the farm! The animals are stressed. (Health -10%)")
                    animal_health -= 10
                
                # Keep variables within limits
                if pasture_quality > 100: pasture_quality = 100
                if animal_health < 0: animal_health = 0
            
            input("\nPress Enter to return to main menu...")

        # --- MENU 4: END MONTH (REVENUE & EXPENSES) ---
        elif choice == '4':
            print("\nEnding the month...")
            
            income = animal_health * 2 
            expenses = 50 
            profit = income - expenses
            
            money += profit
            
            animal_health -= 5
            pasture_quality -= 5
            
            if animal_health < 0: animal_health = 0
            if pasture_quality < 0: pasture_quality = 0

            print(f"Monthly Income: ${income} (based on animal health)")
            print(f"Monthly Expenses: ${expenses}")
            if profit >= 0:
                print(f"Net Profit: +${profit}")
            else:
                print(f"Net Loss: -${abs(profit)}")
                
            print("\nThe animals get a bit hungry and the pasture needs time to grow.")
            
            month += 1
            event_checked = False  # Reset event checker for the new month
            
            input("\nPress Enter to start the next month...")

        # --- QUIT GAME ---
        elif choice == '0':
            print("Thanks for playing! Goodbye.")
            break
        
        else:
            print("Invalid choice! Please enter a number between 0 and 4.")

    # --- ENDINGS LOGIC ---
    if month > 10:
        print("\n" + "*"*40)
        print_slow("GAME OVER! Let's see how you did...")
        print("*"*40)
        
        print(f"Final Money: ${money}")
        print(f"Final Animal Health: {animal_health}%")
        print(f"Final Pasture Quality: {pasture_quality}%\n")
        
        # Ending 1: Sustainable Herder (Golden Ending)
        if money >= 500 and animal_health >= 70 and pasture_quality >= 70:
            print_slow("ENDING: THE SUSTAINABLE HERDER")
            print("Congratulations! You managed to make a profit while keeping the animals happy")
            print("and preserving the environment. You are a true sustainable farmer!")
            
        # Ending 2: Greedy Farmer (Bad Environment Ending)
        elif money >= 1000 and pasture_quality < 40:
            print_slow("ENDING: THE GREEDY FARMER")
            print("You made a lot of money, but at what cost?")
            print("The pasture is destroyed and turned into a desert. This is not sustainable.")
            
        # Ending 3: Bankruptcy (Bad Financial Ending)
        elif money < 0:
            print_slow("ENDING: BANKRUPTCY")
            print("You ran out of money and had to sell the farm.")
            print("Sustainability also means financial stability. Better luck next time!")
            
        # Ending 4: Neutral Ending
        else:
            print_slow("ENDING: AVERAGE FARMER")
            print("You survived the 10 months. The farm is still standing, but there is")
            print("room for improvement in balancing money, health, and nature.")
        
        print("*"*40 + "\n")

# Run the program
if __name__ == "__main__":
    main()