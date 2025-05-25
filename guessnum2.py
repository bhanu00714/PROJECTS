# import random
# number = random.randint(1,100)
# count = 0
# while True:
#     count += 1
#     guess = input("Guess the number between 1 and 100: ")
#     if guess.isdigit() :
#         num = int(guess)
#         if num == number:
#             print("Yoooo Congrats!!")
#             break
#         elif num<number:
#             print("too low")
#         elif num> number:
#             print("too high")  
#     else:
#         print("enter a valid number")  
# if count <= 5:
#     print(f"Congrats you guessed the number in just {count} tries")
# else:
#     print(f"Congrats you guessed the number in {count} tries")         


a = input()
b = a.split(",")
print(b)