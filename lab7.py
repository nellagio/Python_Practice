import random

user = input("You should guess the number between 1 and 10! ")
user = int(user)
computer = random.randint(0, 11)

while True:
    user = int(user)
    if computer < user:
        user = int(input("Guess lower.."))
    elif computer > user:
       user = int(input("Guess higher.."))
    else:
        print("You won!")
        break 

'''
Lab 8: Guess the Number
Let's play 'Guess the Number', the computer will choose a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Advanced Version 1
Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

Advanced Version 2
Keep track of how many guesses the user has made, and tell them at the end.

Advanced Version 3
Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost.

Advanced Version 4
Tell the user whether their current guess is closer than their last.

Super Advanced Version 1
Swap the user with the computer: the user will pick a number, and the computer will guess until they get it right.
'''

# import random

# target = random.randint(1,10)

# guess = ''
# while True:
#     guess = input('guess the number! ')
#     guess = int(guess)
#     if guess == target:
#         print('that\'s correct!')
#         break
#     else:
#         print('that\'s incorrect!')

#     if target > guess:
#         print('guess higher!')
#     else:
#         print('guess lower!')