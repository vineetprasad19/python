from random import randint

# Create a list of play options
t = ["rock", "paper", "scissors"]

# Set player to False initially
player = False

while not player:
    # Ask for the player's choice
    player = input("rock, paper, scissors? (or type 'quit' to exit): ").lower()

    # Exit condition
    if player == "quit":
        print("Thanks for playing!")
        break

    # Assign a random play to the computer
    computer = t[randint(0, 2)]

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    # Reset player to False to continue the loop
    player = False
