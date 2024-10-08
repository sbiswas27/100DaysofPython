# Demo Link: https://appbrewery.github.io/python-day12-demo/

import random

EASY_LEVEL=10
HARD_LEVEL=5

turns = 0

def check_answer(user_guess, correct_answer, turns):
    if user_guess > correct_answer:
        print("Too High.")
        return turns - 1
    elif user_guess < correct_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {correct_answer}")

def difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard'. ").lower()
    if level=='easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    correct_answer= random.randint(1,100)
    turns = difficulty()


    guess = 0
    while guess!=correct_answer:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,correct_answer,turns)
        if turns == 0 :
            print("You have run out of guess, you lose")
            print(f"The answer was {correct_answer}")
            return
        elif guess !=correct_answer:
            print("Guess Again")
        print(f"You have {turns} attempts left to guess the number.")

game()
