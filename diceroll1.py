import random
answer = 1
while answer == 1:
    choise = input("Roll the dice (y/n): ")
    if choise == 'y' or choise == "Y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"({dice1},{dice2})")
    elif choise == "n" or choise == "N":
        print("Thanks for playing!")
        answer = 0
    else:
        print("Invalid choice")