import random

rps = ["Fire", "Water", "Earth"]


def r_p_s():
    selection = random.randint(0, 2)
    return rps[selection]


run = True

print("Human vs Computer. Fire, Water, Earth.")

while run:
    print("\nChoose your element.")
    player_choice = int(input("\nFire(1), Water(2), Earth(3): "))
    player_choice -= 1

    player_selection = rps[player_choice]
    computer_selection = r_p_s()

    print("\nYou selected: " + player_selection)
    print("Computer selected: " + computer_selection)

    if player_selection == computer_selection:
        print("Draw!")
    elif player_selection == "Fire" and computer_selection == "Water":
        print("Computer wins")
    elif player_selection == "Fire" and computer_selection == "Earth":
        print("You win!!!")
    elif player_selection == "Water" and computer_selection == "Earth":
        print("Computer wins")
    elif player_selection == "Water" and computer_selection == "Fire":
        print("You win!!!")
    elif player_selection == "Earth" and computer_selection == "Water":
        print("Computer wins")
    elif player_selection == "Earth" and computer_selection == "Fire":
        print("You win!!!")

    play_again = input("\nPlay again? (y/n): ")
    if play_again == "y":
        continue
    else:
        run = False

