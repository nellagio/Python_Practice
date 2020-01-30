'''

emoticons = [":)", ":(", ":/", "=|"]

num = len(emoticons)

for face in emoticons:
    print(face)

for i in range(5):
    print("Hello, world!")

'''


x = 0
while x < 5:

    x += 1
    if x == 3:
        continue

    print(x, ":)")
    x += 1

    if x == 3:
        break

else:
    print(x, ":(")