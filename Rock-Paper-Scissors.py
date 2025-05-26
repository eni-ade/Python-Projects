# Multiplayer Rock, Paper, Scissors

import getpass
options = ("rock", "paper", "scissors")

while True:
    player1 = getpass.getpass("Player One, Enter a choice (rock, paper, scissors): ")
    player2 = getpass.getpass("Player Two, Enter a choice (rock, paper, scissors): ")

    print("\nChoices.... ")
    print(f"Player One chose {player1}")
    print(f"Player Two chose {player2}")

    if player1 == options[1] and player2 == options[0]:
        print("Player One wins!!!")
    elif player1 == options[0] and player2 == options[2]:
        print("Player One wins!!!")
    elif player1 == options[2] and player2 == options[1]:
        print("Player One wins!!!")
    
    elif player2 == options[1]  and player1 == options[0]:
        print("Player Two wins!!!")
    elif player2 == options[0] and player1 == options[2]:
        print("Player Two wins!!!")
    elif player2 == options[2] and player1 == options[1]:
        print("Player Two wins!!!")
    elif player1 == player2:
        print("You have chosen the same option. Start Over")
    
    play_again = input("\nPlay again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
