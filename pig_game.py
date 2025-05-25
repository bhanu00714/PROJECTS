import random 
def die_through():
    die = random.randint(1,6)
    return die
    
print("WELCOME 😊🐷")
def game_play():
    player_score = [0,0]
    
    index = 0
    chance_score = 0
    while True:
        
        toss = die_through()
        print(f"player {index+1} turn")
        r = input("press r to play: ").strip().lower()
        if r == 'r':
            print(toss)
        else:
            print("invalid choise")  
            continue  
        
        
        if toss == 1:
            print("oops!! better luck nxt time")
            chance_score = 0
            print(f"PLAYER {index+1} SCORE:{player_score[index]}")
           
            if index == 0:
                index = 1
            else:
                index = 0  
            continue     
        else:
            chance_score += toss
        cont_or_not = input("Do you want to continue?(y/n)").strip().lower()
        if cont_or_not == 'n':
            player_score[index] += chance_score
            print(f"PLAYER {index+1} SCORE:{player_score[index]}")
            if index == 0:
                index = 1
            else:
                index = 0   
        elif cont_or_not == 'y':
            continue
        else:
            print("Invalid choise") 
        if player_score[0] >= 20 or player_score[1] >= 20 :
            max_score = max(player_score)
            max_score_holder = player_score.index(max_score)
            print(f"CONGRATS PLAYER {max_score_holder+1} WON WITH A SCORE OF {max_score}")
            break    
        else:
            continue       

game_play()