import random

name_one = input("Please insert first name: ")
one_strength = random.randint(5, 10)
one_health = random.randint(5, 10)
one_magic = random.randint(5, 10)

one_class = ""
one_class_pos = random.randint(1, 3)
if(one_class_pos == 1):
    one_class = "warrior"
elif(one_class_pos == 2):
    one_class = "wizard"
else:
    one_class = "potato"

if(one_class == "warrior"):
    one_strength *= 3
elif(one_class == "wizard"):
    one_magic *= 3
elif(one_class == "potato"):
    one_health *= 3


name_two = input("Please insert second name: ")
two_strength = random.randint(5, 10)
two_health = random.randint(5, 10)
two_magic = random.randint(5, 10)

two_class = ""
two_class_pos = random.randint(1, 3)
if(two_class_pos == 1):
    two_class = "warrior"
elif(two_class_pos == 2):
    two_class = "wizard"
else:
    two_class = "potato"

if(two_class == "warrior"):
    two_strength *= 3
elif(two_class == "wizard"):
    two_magic *= 3
elif(two_class == "potato"):
    two_health *= 3


name_three = input("Please insert third name: ")
three_strength = random.randint(5, 10)
three_health = random.randint(5, 10)
three_magic = random.randint(5, 10)

three_class = ""
three_class_pos = random.randint(1, 3)
if(three_class_pos == 1):
    three_class = "warrior"
elif(three_class_pos == 2):
    three_class = "wizard"
else:
    three_class = "potato"

if(three_class == "warrior"):
    three_strength *= 3
elif(three_class == "wizard"):
    three_magic *= 3
elif(three_class == "potato"):
    three_health *= 3


name_four = input("Please insert forth name: ")
four_strength = random.randint(5, 10)
four_health = random.randint(5, 10)
four_magic = random.randint(5, 10)

four_class = ""
four_class_pos = random.randint(1, 3)
if(four_class_pos == 1):
    four_class = "warrior"
elif(four_class_pos == 2):
    four_class = "wizard"
else:
    four_class = "potato"

if(four_class == "warrior"):
    four_strength *= 3
elif(four_class == "wizard"):
    four_magic *= 3
elif(four_class == "potato"):
    four_health *= 3


name_five = input("Please insert fifth name: ")
five_strength = random.randint(5, 10)
five_health = random.randint(5, 10)
five_magic = random.randint(5, 10)

five_class = ""
five_class_pos = random.randint(1, 3)
if(five_class_pos == 1):
    five_class = "warrior"
elif(five_class_pos == 2):
    five_class = "wizard"
else:
    five_class = "potato"

if(five_class == "warrior"):
    five_strength *= 3
elif(five_class == "wizard"):
    five_magic *= 3
elif(five_class == "potato"):
    five_health *= 3


print("Welcome to the character generator!")
print("Let's meet the brave adventurers:")
print(f"Character 1: {name_one}")
print(f"Character 2: {name_two}")
print(f"Character 3: {name_three}")
print(f"Character 4: {name_four}")
print(f"Character 5: {name_five}")
print("................")
print()
print("***YOUR CHARACTERS ARE COMPLETE***")
print(f"\"{name_one}\" is a {one_class}!")
print(f"\tStrength: {one_strength}")
print(f"\tMagic: {one_magic}")
print(f"\tHealth: {one_health}")
print()
print(f"\"{name_two}\" is a {two_class}!")
print(f"\tStrength: {two_strength}")
print(f"\tMagic: {two_magic}")
print(f"\tHealth: {two_health}")
print()
print(f"\"{name_three}\" is a {three_class}!")
print(f"\tStrength: {three_strength}")
print(f"\tMagic: {three_magic}")
print(f"\tHealth: {three_health}")
print()
print(f"\"{name_four}\" is a {four_class}!")
print(f"\tStrength: {four_strength}")
print(f"\tMagic: {four_magic}")
print(f"\tHealth: {four_health}")
print()
print(f"\"{name_five}\" is a {five_class}!")
print(f"\tStrength: {five_strength}")
print(f"\tMagic: {five_magic}")
print(f"\tHealth: {five_health}")



