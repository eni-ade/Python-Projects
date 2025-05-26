import random
r1 = random.randint(1, 20)
user_input = int(input("Please enter a number from 1 - 20: "))
while user_input != r1:
    if user_input > r1:
        print('Number is too high')
    elif user_input < r1:
        print("Number is too low")
    user_input = int(input("Try again, Enter a number from 1 - 20: "))

print("Congratulations, You are correct🙂")

