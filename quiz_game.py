print("WELCOME TO THE QUIZ!!")
playing = input("Do you want to play(y/n): ").lower()
if playing != 'y':
    quit()
#questions
q_a = [["What do you call a fake noodle?","An Impasta"
,"A Ramen-tic","A Spaghetti Faker",
"A Maca-phoney"],
[" If a tomato is a fruit, then what does that make ketchup?",
"A smoothie",
"A salad dressing",
"A vegetable juice",
"A mistake"],
["What did one wall say to the other wall?",
"“I’ll corner you later.”",
"“We’ll meet at the corner.”",
"“Nice to be on the same side.”",
"“Hold up, I’m cracking!”"],
["Why don’t skeletons fight each other?",
"They don’t have the guts",
"They’d just fall apart",
"They’re all boneheads",
"They’d just laugh their ribs off"],
[" If you drop a yellow hat in the Red Sea, what will it become?",
 "Wet","Orange","Lost","A fish’s new home"]
]
#Answers
ans = {
    q_a[0][0] :q_a[0][1],
    q_a[1][0] :q_a[1][1],
    q_a[2][0] :q_a[2][2],
    q_a[3][0] :q_a[3][1],
    q_a[4][0] :q_a[4][1]
    
}
#logic
score = 0
for i in range(len(q_a)):
    print(f"{q_a[i][0]}\n1.{q_a[i][1]}\n2.{q_a[i][2]}\n3.{q_a[i][3]}\n4.{q_a[i][4]}")
    answer_int = 0
    while True:
        answer_int = int(input("Enter the index: "))
        if answer_int not in  range(1,5):
            print("Enter a valid index")
            print(answer_int)
            continue

        else:
            break    
        
    print("_"*25)
    answer_alpha = q_a[i][answer_int]
    if ans[q_a[i][0]] == answer_alpha:
        score = score+1


#printing the score   
print(f"Your Score: {score}/{len(q_a)}")      
print("Version 2")
print("Version 3")