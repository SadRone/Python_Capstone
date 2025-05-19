print("BLACKJACK")
import random
print("Add up the cards to the largest number with the limit 21. IF you go over 21, you lose")
print("J Q K counts as 10, A can be counted as 1 or 11")
print("It begins with the random two cards, you can get one more card and play it or just play")
print("Starting the game intro: \n")



def deal_card():
    """Return a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return and return the score calculated form the card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "Lose, computer has a blackjack"
    elif u_score == 0:
        return "Win, you have a blackjack"
    elif u_score > 21:
        return "Lost, user over 21"
    elif c_score > 21:
        return "Won, computer over 21"
    elif u_score > c_score:
        return "You won"
    else:
        return "you lost"


def play_game():
    """add default cards for user and computer with empty list (empty handed)"""
    user_cards = []
    computer_cards = []
    computer_score = -1 #BlackJack = 0
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())  # += only available for integers / use .append for single value to be added

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_score}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            ask = input("Type y to get another card or n to pass")
            if ask == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand {computer_cards} and final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack?? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()