import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)
print(computer_choice)
if user_choice >= 3 or user_choice < 0:
    print("user choice is invalid ,you lose !")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print(" You Lose !")
elif user_choice > computer_choice:
    print("YOU WIN!")
elif user_choice < computer_choice:
    print(" You Lose!")
elif user_choice == computer_choice:
    print("it's Draw")
