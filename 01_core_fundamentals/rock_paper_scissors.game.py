import random
choices = ["rock", "paper", "scissors"]
draw = random.choice(choices)
player_choice = input("Rock, paper, or scissors? ").lower()
if draw == "rock" and player_choice == "scissors":
    print("I chose rock, you lose!")
elif draw == "paper" and player_choice == "rock":
    print("You lose, I chose paper!")
elif draw == "scissors" and player_choice == "paper":
    print("You lose, I chose scissors!")
elif draw == "rock" and player_choice == "paper":
    print("You win! I chose rock.")
elif draw == "paper" and player_choice == "scissors":
    print("You win! I chose paper")
elif draw == "scissors" and player_choice == "rock":
    print("You win! I chose scissors.")
elif draw == player_choice:
    print("It is a draw! We both picked",draw,"!")