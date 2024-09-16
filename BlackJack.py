#Task: Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.



import random
from art import logo
def deal_card():
    """choose a random card from the card list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(card_list):
    """Take a list of card, apply the blackjack rules and calculate a score for user and dealer"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0

    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "User Lose, dealer has a blackjack"
    elif u_score == 0:
        return "User Wins with a blackjack"
    elif c_score > 21:
        return "Dealer went over, User Wins!"
    elif u_score > c_score:
        return 'User Wins!'
    else:
        return "User lose!"



def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    is_game_over = False

    for _ in range(2):
        """Choose 2 random cards each for the user and the dealer(computer)"""
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current_score: {user_score}")
        print(f"Computer's card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_response = input("Do you want to draw another card? Type 'y' for yes and 'n' for no.").lower()
            if user_response =='y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards} & your final score: {user_score} ")
    print(f"Computer final cards: {computer_cards} & computer's final score: {computer_score} ")
    print(compare(user_score,computer_score))



while input("Do you want to play a game of Blackjack? Type 'y' for Yes and 'n' for No.") == 'y':
    print('\n' * 20)
    play_game()
