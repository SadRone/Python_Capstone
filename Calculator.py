print(''' 
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

continue_process = False
while continue_process == False:
    number1 = float(input("pick a first number: "))
    operation = (input("Pick an operation: [ +, -, /, x ] "))
    number2 = float(input("pick a second number: "))


    if operation == "+":
        print(number1 + number2)
    elif operation == "-":
        print(number1 - number2)
    elif operation == "/":
        print(number1 / number2)
    elif operation == "x":
        print(number1 * number2)
    else:
        print("wrong input")

    print("DO you want to use calculator once more?")

    user_input = input("yes or no ?").lower()
    if user_input == "yes":
        continue_process = False
    else:
        continue_process = True