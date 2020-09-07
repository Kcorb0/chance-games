import random


def coin_flip():
    user_input = int(input("How many flips: "))
    count = user_input
    head_count = 0
    tail_count = 0


    while count != 0:
        flip = random.choice([1, 2])
        if flip == 1:
            print("heads")
            head_count += 1
        else:
            print("tails")
            tail_count += 1
        count -= 1

    print("\nTotal Heads: " + str(head_count))
    print("Total Tails: " + str(tail_count))


while True:
    coin_flip()

    again = input("\nFlip again? y/n: ")
    if again == "n":
        break
    else:
        continue
