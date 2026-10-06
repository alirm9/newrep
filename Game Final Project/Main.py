# Sustainable Herder - Text Adventure Game
# A game about balancing profit, animal welfare, and nature.

import sys
import time
import random

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

def manage_food(money, animal_health):
    """Handles the food purchasing logic."""
    print("\n[ Menu: Food Management ]")
    print("1. Cheap industrial food ($50, Health -5%)")
    print("2. Organic feed ($150, Health +10%)")
    print("0. Cancel and return")
    
    choice = input("Select an option (0-2): ")
    
    if choice == '1':
        if money >= 50:
            print("Result: You bought cheap industrial food. The animals don't look very happy.")
            return money - 50, animal_health - 5
        else:
            print("Result: Not enough money!")
    elif choice == '2':
        if money >= 150:
            print("Result: You bought organic feed. The herd looks healthy and energetic!")
            return money - 150, animal_health + 10
        else:
            print("Result: Not enough money!")
    elif choice == '0':
        print("Returning to main menu...")
    else:
        print("Invalid choice.")
        
    return money, animal_health

def manage_pasture(money, pasture_quality):
    """Handles the pasture management logic."""
    print("\n[ Menu: Pasture Management ]")
    print("1. Free Grazing (Cost: $0, Pasture Quality -15%)")
    print("2. Rotational Grazing (Cost: $100, Pasture Quality +10%)")
    print("0. Cancel and return")
    
    choice = input("Select an option (0-2): ")
    
    if choice == '1':
        print("Result: You let the herd roam freely. The land is overgrazed and heavily damaged.")
        return money, pasture_quality - 15
    elif choice == '2':
        if money >= 100:
            print("Result: You set up fences for rotational grazing. The pasture has time to recover!")
            return money - 100, pasture_quality + 10
        else:
            print("Result: Not enough money for fencing!")
    elif choice == '0':
        print("Returning to main menu...")
    else:
        print("Invalid choice.")
        
    return money, pasture_quality

def check_events(money, animal_health, pasture_quality):
    """Handles random monthly events."""
    print("\n[ Menu: Farm Events ]")
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
        
    return money, animal_health, pasture_quality

def calculate_endings(money, animal_health, pasture_quality):
    """Evaluates the final score and determines the ending."""
    print("\n" + "*"*40)
    print_slow("GAME OVER! Let's see how you did...")
    print("*"*40)
    
    print(f"Final Money: ${money}")
    print(f"Final Animal Health: {animal_health}%")
    print(f"Final Pasture Quality: {pasture_quality}%\n")
    
    if money >= 500 and animal_health >= 70 and pasture_quality >= 70:
        print_slow("ENDING: THE SUSTAINABLE HERDER")
        print("Congratulations! You managed to make a profit while keeping the animals happy")
        print("and preserving the environment. You are a true sustainable farmer!")
    elif money >= 1000 and pasture_quality < 40:
        print_slow("ENDING: THE GREEDY FARMER")
        print("You made a lot of money, but at what cost?")
        print("The pasture is destroyed and turned into a desert. This is not sustainable.")
    elif money < 0:
        print_slow("ENDING: BANKRUPTCY")
        print("You ran out of money and had to sell the farm.")
        print("Sustainability also means financial stability. Better luck next time!")
    else:
        print_slow("ENDING: AVERAGE FARMER")
        print("You survived the 10 months. The farm is still standing, but there is")
        print("room for improvement in balancing money, health, and nature.")
    
    print("*"*40 + "\n")

def clamp_values(health, pasture):
    """Keeps health and pasture values between 0 and 100."""
    if health > 100: health = 100
    if health < 0: health = 0
    if pasture > 100: pasture = 100
    if pasture < 0: pasture = 0
    return health, pasture

def main():
    month = 1
    money = 1000
    animal_health = 50
    pasture_quality = 50
    event_checked = False 

    print_slow("Welcome to 'The Sustainable Herder'!")
    print_slow("You have inherited a small herd of sheep and a damaged pasture.")
    print_slow("Your goal: Survive 10 months, make money, but keep the animals healthy and save the nature.\n")

    while month <= 10:
        animal_health, pasture_quality = clamp_values(animal_health, pasture_quality)
        show_status(month, money, animal_health, pasture_quality)
        
        print("What do you want to do this month?")
        print("1. Buy food for the herd")
        print("2. Manage the pasture (grazing)")
        print("3. Check farm events (Once per month)")
        print("4. End the month and go to the next")
        print("0. Quit Game")
        
        choice = input("Enter your choice (0-4): ")

        if choice == '1':
            money, animal_health = manage_food(money, animal_health)
            input("\nPress Enter to return to main menu...")
            
        elif choice == '2':
            money, pasture_quality = manage_pasture(money, pasture_quality)
            input("\nPress Enter to return to main menu...")
            
        elif choice == '3':
            if event_checked:
                print("\nYou have already checked for events this month. Wait until next month!")
            else:
                money, animal_health, pasture_quality = check_events(money, animal_health, pasture_quality)
                event_checked = True
            input("\nPress Enter to return to main menu...")
            
        elif choice == '4':
            print("\nEnding the month...")
            income = animal_health * 2 
            expenses = 50 
            profit = income - expenses
            
            money += profit
            animal_health -= 5
            pasture_quality -= 5
            
            print(f"Monthly Income: ${income} (based on animal health)")
            print(f"Monthly Expenses: ${expenses}")
            if profit >= 0:
                print(f"Net Profit: +${profit}")
            else:
                print(f"Net Loss: -${abs(profit)}")
                
            print("\nThe animals get a bit hungry and the pasture needs time to grow.")
            
            month += 1
            event_checked = False
            input("\nPress Enter to start the next month...")
            
        elif choice == '0':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice! Please enter a number between 0 and 4.")

    if month > 10:
        animal_health, pasture_quality = clamp_values(animal_health, pasture_quality)
        calculate_endings(money, animal_health, pasture_quality)

if __name__ == "__main__":
    main()