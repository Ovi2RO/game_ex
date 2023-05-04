import random

def char_class():
    one_class = ""
    one_class_pos = random.randint(1, 3)
    if(one_class_pos == 1):
        one_class = "Barbarian"
    elif(one_class_pos == 2):
        one_class = "Cleric"
    else:
        one_class = "Druid"

    return one_class


print("Welcome to the character generator!")
character_no = int(input("How many characters do you want to create? "))

char_range = range(0, character_no)

name_list = []

for char in char_range:
    player_name = input("Give me an name: ")
    name_list.append(player_name)

print("Let's name the brave adventurers:")
char_counter = 1
for name in name_list:
    print(f"Character {char_counter}: {name}")
    char_counter += 1

print("***YOUR CHARACTERS ARE COMPLETE***")

for name in name_list:
    p_class = char_class()
    print(f"{name} is a {p_class}")
    one_strength = random.randint(3, 15)
    one_health = random.randint(3, 15)
    one_magic = random.randint(3, 15)
    one_initiative = random.randint(3, 15)
    if(p_class == "Barbarian"):
        one_strength *= 3 
        one_health *= 3
    elif(p_class == "Cleric"):
        one_magic *= 3 
        one_initiative *= 3
    else:
        one_magic *= 2
        one_initiative *= 2
        one_health *= 2
    
    print("Strength:", one_strength)
    print("Magic:", one_magic)
    print("Health:", one_health)
    print("Initiative:", one_initiative)
    print("*" * 10)

print("Happy adventuring!")



