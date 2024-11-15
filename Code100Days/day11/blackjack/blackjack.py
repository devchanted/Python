import random
from art import logo

# create a deal card function

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# create a play game and assign two cards to user and computer

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        print("Blackjack")
    else:
        print("No blackjack")

def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(user_cards)
    print(computer_cards)
    

play_game()

