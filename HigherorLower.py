# thought process to tackle the problem
#Display Art
# import the data
# Get two random dicts from the list - A and B (name,description,country)
#Format the account data into a printable format
# compare the follower count for A Vs B
# ask user to input their answer:
# if the user is wrong, game over - print the final score -- so need to maintain a score for every right answer
# if the user is right, choose one random dict apart from already chosen ones
#When the user is right, B becomes A and we choose another random dict which will become B
#keep adding the score

from art import logo,vs
from game_data import data
import random

# Function to format the account naming,description as per the game
def format_accounts(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# Function to check if the user's guess is right or wrong by comparing the follow count
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

print(logo)

# Maintaing a score for the user and the game
score = 0

game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #Choosing two random accounts to compare
    #We also need to make sure that the account_b comes to position a for next round if the user's guess was right
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)



    print(f"Compare A : {format_accounts(account_a)}.")
    print(vs)
    print(f"Against B : {format_accounts(account_b)}.")

    #Asking the user for their input/guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Clear the screen
    print("\n" *20)
    print(logo)

    #assinging variables for the follow count of 2 accounts to call the function that checks the correct answer
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score +=1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

