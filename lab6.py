import random 

character = ["rock", "paper", "scissors"]
play_again = "yes"

while play_again == "yes":

    play_choice = input("choose a player: rock, paper or scissors? ")

    computer = random.choice(character)

    if play_choice == "rock" and computer == "rock":
        print("Tie!")

    elif play_choice == "paper" and computer == "rock":
        print("You win!")

    elif play_choice == "scissors" and computer == "rock":
        print("Computer wins!")

    elif play_choice == "rock" and computer == "paper":
        print("Computer wins!")

    elif play_choice == "paper" and computer == "paper":
        print("Tie!")

    elif play_choice == "scissors" and computer == "paper":
        print("You wins!")

    elif play_choice == "rock" and computer == "scissors":
        print("You win!")

    elif play_choice == "paper" and computer == "scissors":
        print("Computer wins!")

    elif play_choice == "scissors" and computer == "scissors":
        print("Tie!")

    else:
        print("goodbye!")
        break 

    play_again = input("Do you want to play again? ")