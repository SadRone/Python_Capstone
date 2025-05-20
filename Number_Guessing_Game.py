import random

print(''' Welcome to the number guessing game \n
You will guess the number from 1 to 10, and if you lose \n
you will get an infinite loop that might damage your pc memory with high computation
else, you will win and survive. You have 5 attempts, Let's go : ''')
infinite = True
continue_running = True
life = 5
numbers = random.randint(1,10)

while continue_running:
    while life:
        user = int(input("write the number from 1 to 10: "))
        if user == numbers:
            print("You have survived, good to go")
            continue_running = False
        else:
            life -=1
            print(f"You have {life}, try again")

    if life == 0:
        infinite = True
        print("BUUUUUUUUUUUUUUUUUG")
