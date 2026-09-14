import random

def roll_custom_dice(sides):
    return random.randint(1, sides)

# Main program
max_sides = int(input("Enter the number of sides on the dice: "))

result = 0
while result != max_sides:
    result = roll_custom_dice(max_sides)
    print(f"Rolled: {result}")