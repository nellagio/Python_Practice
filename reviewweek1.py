


# print("Hello")

# spoon = input("Hello ")

# print(spoon)

# fork = 4 #integer 
# butter_knife = 2.4  #float

# straw = True #boolean

# super_heros = ["antman", "batman", "wonderwoman", "catwoman", "thor", "flash"] #list (blank)

# fav_hero = input("what is your favorite super hero? ")

# while True:
#     play_again = input("What's your favorite super hero? ")
#     if fav_hero not in super_heros:
#         super_heros.insert(0, fav_hero)
#     else:
#         print(super_heros)
#         break
import random
import string

letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
new_word = random.choice(letters)*3

for i in range (5):
    print(letters)