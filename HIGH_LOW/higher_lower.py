from logo import l
from logo import s
from test import dict
import random

print(l)
score = 0
def format_data(account):
    """Takes the account data and returns the principles format"""
    account_name = account_a["name"]
    account_desc = account_a["description"]
    account_count = account_a["country"]
    return f"{account_name}, a {account_desc}, from {account_count}"

def check_answer(user_guess, a_follower, b_follower):
    """take a user's guess  and the follower counts and returns if they got it right."""
    if a_follower > b_follower:
        return choice == 'a'
    else:
        return choice == 'b'
account_b = random.choice(dict)
account_a = random.choice(dict)

cont_game = True
while cont_game:



    account_a = account_b
    account_b = random.choice(dict)

    if account_a == account_b:
        account_b = random.choice(dict)

    print(f"Compare A: {format_data(account_a)} \n")
    print(s)
    print(f"Compare B: {format_data(account_b)} \n")

    choice = input("Who has more followers ? A or B: ").lower()

    print("\n" * 20)
    print(l)

    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]
    is_correct = check_answer(choice, a_follower_count, b_follower_count)

    if is_correct:
        print(account_a["followers"])
        print(account_b["followers"])
        score += 1
        print(f"You're right with current score:{score}")
        cont_game = False
    else:
        print(account_a["followers"])
        print(account_b["followers"])
        print(f"You are wrong with last score :{score}")
        cont_game = False