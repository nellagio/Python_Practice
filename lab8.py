import random 
import string

print("random password generator:")

random_letters = string.ascii_letters + string.digits + string.punctuation
new_password = ""
for np in range(10):
    new_password += random.choice(random_letters)
print(new_password)