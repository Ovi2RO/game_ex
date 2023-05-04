from Char_stat import Char_stat
from Char_class import Char_class


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

print()
print("***YOUR CHARACTERS ARE COMPLETE***")
print()

count = len(name_list)

for name in name_list:
    player = Char_stat()
    player_c = Char_class.c_class()
    print(f"{name} is a {player_c}")
    print(f"\tStrength:",player.c_strength(player_c))
    print(f"\tHealth:",player.c_health(player_c))
    print(f"\tMagic:",player.c_magic(player_c))
    print(f"\tInitiative:",player.c_initiative(player_c))
    print("*" * 10)
    count -= 1

print()
print("Happy adventuring!")

