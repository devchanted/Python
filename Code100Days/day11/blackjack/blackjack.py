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
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(user_cards)
    print(computer_cards)


    u_score = calculate_score(user_cards)
    c_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {u_score}")
    print(f"Computer's first card: {computer_cards[0]}")



play_game()

