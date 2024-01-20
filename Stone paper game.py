import random
rock = '''
STONE
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]
user_input = int(input("Enter your choice: 0 for STONE, 1 for PAPER, 2 for SCISSORS\n"))
if user_input<0 or user_input>2:
    print("Envalid Choice")
else:
    computer_choice = random.randint(0, 2)
    print("You Choose: " + image[user_input])
    print("Computer Choose: " + image[computer_choice])
    if user_input == computer_choice:
        print("Game is Draw")
    elif user_input==0 and computer_choice==1:
        print("You Lost!")
    elif user_input==1 and computer_choice==2:
        print("You Lost!")
    elif user_input==2 and computer_choice==0:
        print("You Lost!")
    else:
        print("You Win!")