import random

words = ['camel', 'penguin' , 'dog' , 'cat' , 'seungbeom']

lives = 6

answer = random.choice(words)
print(answer)

placeholder = ""
for position in range(len(answer)):
    placeholder += "_"
print(placeholder)

correct_letters = []
game_over = False

while not game_over:




    print(f"You have {lives} left out")
    user_input = input(str("Guess the word, type a character: ")).lower()
    print(user_input)

    if user_input in correct_letters:
        print(f" there is alrady {user_input}")

    display = ""



    for letter in answer:
        if letter == user_input:
            display += letter
            correct_letters.append(user_input)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if user_input not in answer:
        lives -= 1
        print(f" There is no {user_input} in the words")
        if lives == 0:
            game_over = True
            print("You lost")
            print(f"The answer was {answer}")

    if "_" not in display:
        print("You won")
        game_over = True


