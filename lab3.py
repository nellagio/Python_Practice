'''
Instructions

Let's write a program to simulate the classic "Magic Eight Ball"

    Print a welcome screen to the user.
    Prompt the user to ask the 8-ball a question.

    For example: "Will I win the lottery tomorrow?"

    Use the random module's random.choice() to choose a prediction.
    Display the result of the prediction.

Advanced version 1

    Let the user choose if they want to ask a second question.

Advanced version 2

    Ask the user if they want to ask another question, using a while loop.
'''
import random 

print("Welcome to Magic 8 ball")

input("Ask me a question?")

eight_ball_answers = ["Yes", "Of course", "Not a chance...", "Better luck asking something else"]

random.choice(eight_ball_answers)

print(random.choice(eight_ball_answers))

print("so,")
input("would you like to try again?")

("yes") 

input("Ask me a question?")

print(random.choice(eight_ball_answers))
