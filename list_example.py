import random 

'''

my_list = ["crimson", "violet", "teal", "pink", "grey"]

for llama in my_list:
    print(llama) #prints colors in a column

for color in my_list:
    print(color, "is cool") #prints colors in a column with (is cool) at the end
'''

grades = [98, 74, 36, 88, 70]

grades.append(69)

#print(grades)

grades.pop(2)

#print(grades)

i = grades.index(69)

grades.pop(i)

#print(grades)

grades.insert(2, "apple")

#print(grades)


print(random.choice(grades))

print(random.randint(0, 10))