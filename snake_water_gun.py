import random

snake = "🐍"
water = "💧"
gun = "🔫"

game_emojis = [snake, water, gun]
user_choice = int(input("Enter your choice:\n 0 for Snake\n 1 for water\n 2 for gun"))
if user_choice>2 or user_choice<0:
    print("Invalid choice")
else:
    print("You choose:",game_emojis[user_choice])
    computer_choice = random.randint(0,2) 
    print("Computer choose:",game_emojis[computer_choice])
    if computer_choice == user_choice:
        print("Draw")
    elif (user_choice == 0 and computer_choice == 1) or\
         (user_choice == 2 and computer_choice == 0) or\
         (user_choice == 1 and computer_choice == 2):
        print("User Wins")
    else:
        print("Computer wins")

#rules :
#       snake wins against water
#       gun wins against snake
#       water wins against gun
