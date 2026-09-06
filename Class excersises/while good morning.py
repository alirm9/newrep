##rounds = int(input("How many greetings: "))
##finished_rounds = 0
##while finished_rounds<rounds:
    ##print("Good morning")
    ##finished_rounds = finished_rounds + 1

##command = input("enter command: ")
##while command != "stop":
    ##print("You entered: ", command)
    ##command = input("enter command: ")
##print("execution stopped")

##import random
##dice1 = dice2 = rolls = 0
##while (dice1 != 6 or dice2 != 6):
    ##dice1 = random.randint(1,6)
    ##dice2 = random.randint(1,6)
    ##rolls += 1
##print(f" rolled {rolls:d} times.")

import random
rounds = 0
total_rolls = 0
while rounds < 100000:
    dice1 = dice2 = rolls = 0
    while ( dice1 != 6 or dice2 != 6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls += 1
    total_rolls += rolls
    rounds += 1
average_rolls = total_rolls / rounds
print(f"Average rolls to get double sixes: {average_rolls:.2f}")

