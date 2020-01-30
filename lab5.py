import random

eyes = ['8', ':', ';', "=", "I"]
noses = [">", "-"]
mouths = ["o", "O", ")", "(", "D", "P"]
while True:

    for emoji in range(5):
        eye = random.choice(eyes)
        nose = random.choice(noses)
        mouth = random.choice(mouths)

        face_display = eye + nose + mouth

        print(face_display)

    else:
        something = input("do you want to continue? ")

        if something == "yes":
            print(face_display)

        else:
            break