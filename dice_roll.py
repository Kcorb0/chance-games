import random


def dice_roll(num_dice):
    """Rolls number between 1 and 6 using the random module"""
    outcomes = []
    roll_num = 0

    while num_dice != 0:
        num_dice -= 1
        die = random.randint(1, 6)
        outcomes.append(die)

    for outcome in outcomes:
        roll_num += 1
        print("Dice " + str(roll_num) + ": " + str(outcome))

    total = sum(outcomes)
    print("Dice sum: " + str(total))


print("\n#### DICE ROLLER SIM ####")

while True:
    user_input = int(input("\nHow many dice do you wish to roll: "))
    dice_roll(user_input)

    roll_again = input("\nDo you want to roll again? y/n:")

    if roll_again == "y":
        continue
    elif roll_again == "n":
        break
    else:
        print("Enter (y or n)")

