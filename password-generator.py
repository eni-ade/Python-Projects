# password generator

import random
import string

is_running = True

while is_running:
    print()
    print("Welcome to the Password Generator Program.")
    user_input = input("Generate a password (Y/N): ").upper()
    print()

    chars = " " + string.ascii_letters + string.digits + string.punctuation

    chars = list(chars)

    random.shuffle(chars)

    num_chars = int(input("Enter the amount of characters you want: "))

    selected_chars = chars[:num_chars]


    if user_input == "N":
        break
    elif user_input == "Y" and num_chars <= 12:
        print("Password generated is:", "".join(selected_chars))
    elif num_chars > 12:
        print("Too much characters, Please choose a shorter amount.")
    else:
        print("Please enter Y or N")
        
print("Bye for now!")

