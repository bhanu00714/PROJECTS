import random
count = 0
user_won = 0
comp_won = 0
emojis = {'r': '👊','p':'✋','s':'✌'}
elements = ('r','p','s')

print("WELCOME TO ROCK PAPER SCISSORS GAME")
def computer():
    comp_choice = random.choice(elements)
    return comp_choice         
def game(count,user_won,comp_won):
    count += 1
    comp = computer()
    choice = input("Choose (r,p,s): ").lower()

    if choice in elements: 
         print(f"You choose {emojis[choice]}\n Computer choose {emojis[comp]}")
         if choice == comp:
              print("TIE")
         elif ((choice == 'r' and comp == 'p') 
              or (choice == 'p' and comp == 's') 
              or (choice == 's' and comp == 'r')):
              print("YOU LOOSE")
              comp_won += 1
              return comp_won 
         else:
              print("YOU WIN!!")  
              user_won += 1    
              return user_won
        # if choice == 'r':
        #     print(" Your choice is ROCK")
        #     if comp == 'r':
        #         print("Computer choice is also ROCK\n")
        #         print("TIE")
        #     if comp == 'p':
        #         print("Computer choice is PAPER")
        #         print("YOU LOOSE")
        #     if comp == 's':    
        #             print("Computer choice is SCISSORS")
        #             print("YOU WIN!!")
        # elif choice == 'p':
        #     print(" Your choice is PAPER")
        #     if comp == 'r':
        #         print("Computer choice is also ROCK")
        #         print("YOU WIN!!")
        #     if comp == 'p':
        #         print("Computer choice is PAPER")
        #         print("TIE")
        #     if comp == 's':    
        #             print("Computer choice is SCISSORS")
        #             print("YOU LOOSE")
        # elif choice == 's':
        #     print(" Your choice is SCISSORS")
        #     if comp == 'r':
        #         print("Computer choice is also ROCK")
        #         print("YOU LOOSE")
        #     if comp == 'p':
        #         print("Computer choice is PAPER")
        #         print("YOU WIN!!")
        #     if comp == 's':    
        #         print("Computer choice is SCISSORS")
        #         print("TIE")
            
    else:
            print("invalid choice!")
    return count,user_won,comp_won        
        
while True:
        game(count,user_won,comp_won)
        print(count,user_won,comp_won   )
        next = input("Do you want to continue (y/n)?: ").lower()
        if next == 'y' or next == 'n':
            if next == 'n':
                print("Thanks for playing")
                print(f"Number of matches:{count}")
                print(f"Your Score: {user_won}")
                print(f"Computer Score: {comp_won}")
                break
           
        else:
            print("invalid choice!")    