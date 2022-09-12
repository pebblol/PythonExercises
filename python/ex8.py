# ex 8

# Two player Rock Paper Scissors game

def rockpaperscissors(p1, p2):
    if (p1 == "rock" and p2 == "scissors"):
        print("Result: Player 1 wins.")
    elif (p1 == "rock" and p2 == "paper"):
        print("Result: Player 2 wins.")
    elif (p1 == "paper" and p2 == "rock"):
        print("Result: Player 1 wins.")
    elif (p1 == "paper" and p2 == "scissors"):
        print("Result: Player 2 wins.")
    elif (p1 == "scissors" and p2 == "rock"):
        print("Result: Player 2 wins.")
    elif (p1 == "scissors" and p2 == "paper"):
        print("Result: Player 1 wins.")
    elif (p1 == p2):
        print("Result: Draw.")

quit = ""
while (quit != "y"):
    p1 = input("Player 1: Rock, paper, or scissors? ")
    while (p1 != "rock" and p1 != "paper" and p1 != "scissors"):
        p1 = input("Wrong input. Player 1: Rock, paper, or scissors? ")

    p2 = input("Player 2: Rock, paper, or scissors? ")
    while (p2 != "rock" and p2 != "paper" and p2 != "scissors"):
        p2 = input("Wrong input. Player 1: Rock, paper, or scissors? ")

    rockpaperscissors(p1, p2)

    quit = input("Enter 'y' to quit or 'n' to start a new game. ")
