"""Lab 4: Grading

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

    Have the user enter a number representing the grade (0-100)
    Convert the number grade to a letter grade

Numeric Ranges

    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: F

Advanced Version 1

Use randint() from the random module to determine the user's rival's score. Let the user know if they did better than their rival.
Advanced Version 2

Use % to get the remainder of the grade when divided by ten, which is the same as the number in the ones digit. The number in the ones digit will determine whether they will get a '+' or a '-' appended to the end of their grade. For example, the grade 81 would be a 'B'. 81 % 10 would give you 1, which is a low number, so you would add a '-' to the end of the grade.
"""

'''
user = input ("do you think cats are cute? ").lower()

if user == "yes":
    print("I think cats are cute too. ")

elif user == "no":
    print("Get out of my house! ")

else:
    print("invalid opition ")
'''
'''
print("welcome to high school!")
response = int(input("Enter your grade: "))

if response <= 59:
    print("F")

elif response <= 69:
    print("D")

elif response <= 79:
    print("C")

elif response <= 89:
    print("B")

elif response <= 100:
    print("A")

'''
import random


print("Welcome to high school!")

grade = input("Enter your grade: ")
grade = int(grade)
rival = random.randint(0, 100)

if grade >= 90 and grade <= 100:
    print("A")

elif grade >= 80 and grade <=89:
    print("B")

elif grade >=70 and grade <= 79:
    print("C")

elif grade >=60 and grade <=69:
    print("D")

elif grade >= 0 and grade <=59:
    print("F")

else:
    print("You cheater!")

if grade < rival:
    print(f"your rival got a {rival} they beat you this time, better study!")

elif grade > rival:
    print(f"Your rival has been defeated, they got a {rival}")

else:
    print("you were equally matched.")

