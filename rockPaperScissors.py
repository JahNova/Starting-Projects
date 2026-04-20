import random

options=["rock","paper","scissors"]

#user chooses
print("Rock, Paper, Scissors")
player=input("Choose: ")

#computer chooses
ai=random.choice(options)
print(f"AI: {ai}")

#check for winner
if ai == player:
    print("Draw")
elif player == "rock":
    if ai == "scissors":
        print("player wins")
    else:
        print("Ai wins")
elif player == "paper":
    if ai == "rock":
        print("player wins")
    else:
        print("Ai wins")
    print("player wins")
elif player == "scissors":
    if Ai == "paper":
        print("Player wins")
    else:
        print("Ai wins")
