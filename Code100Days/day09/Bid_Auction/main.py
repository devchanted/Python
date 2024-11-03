
import art
print(art.logo)

bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while continue_bidding == True:
    name = input("Enter your Name: ")
    price = int(input("Enter your Bid: $"))
    bids[name] = price
    print(bids)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' . \n ").lower()
    if should_continue == "no" :
        print(should_continue)
        continue_bidding = False
        print(continue_bidding)
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)




