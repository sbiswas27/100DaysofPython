#Task: Build a Rock, Paper, Scissors game.
# DEmo Link - https://appbrewery.github.io/python-day4-demo/

#With ASCII code the signs were already built in the system
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

import random

#Ask user for their input
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(paper)
else:
    print(scissors)

#Let the computer choose randomly
choices_list = [rock,paper,scissors]

computer_random_number=random.randint(0,2)
computer_choice = choices_list[computer_random_number]
print(f"Computer chose : {computer_choice}")

if user_choice==0:
    if computer_random_number==0:
        print("It's a draw :| ")
    elif computer_random_number==1:
        print("You lose :( ")
    else:
        print("You Win!! :D ")
elif user_choice==1:
    if computer_random_number==0:
        print("You Win!! :D ")
    elif computer_random_number==1:
        print("It's a draw :| ")
    else:
        print("You lose :(")
elif user_choice==2:
    if computer_random_number==0:
        print("You lose!! :( ")
    elif computer_random_number==1:
        print("You Win!! :D ")
    else:
        print("It's a draw :| ")





