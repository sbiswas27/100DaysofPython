# Task: The goal is to build a blind auction program.

# Function to get the highest bidder when there are no other bidders left
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bidding price of ${highest_bid}")

#creating an empty dictionary to add all the bidder names as key and their price as value
bids={}

bidding_continues = True

while bidding_continues:
    user_name = input("What's your name?")
    user_bid = int(input("What's your bid price? $"))
    bids[user_name] = user_bid
    should_continue = input("Are there any more bidders in the room? Type 'yes' or 'no'\n").lower()

    if should_continue == 'no':
        bidding_continues = False
        find_highest_bidder(bids)
    else:
        print('\n' * 100)
