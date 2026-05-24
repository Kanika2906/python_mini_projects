import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock,paper,scissors]
user_choice = int(input("Enter your choice:\n 0 for Rock \n 1 for Paper \n 2 for Scissors"))

if user_choice < 0 or user_choice >2:
    print("Invalid choice")
else:
    print("User Choose:",game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer Choose:",game_images[computer_choice])

    if user_choice == computer_choice:
        print("Draw")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 0):
         print("User wins.")
    else:
        print("Computer wins.")
print("Thank you for playing.")



# Rules: 
#        Rock wins against scissors
#        Scissors wins against paper
#        Paper wins against rock