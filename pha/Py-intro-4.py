import random

print("Welcome to character generator!")
print("Let's name the brave adventures: ")


name1 = input("Character 1: ")
name2 = input("Character 2: ")
name3 = input("Character 3: ")
name4 = input("Character 4: ")
name5 = input("Character 5: ")


luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)
if(luck == 1):
    print(name1 + " is a Warrior")
    strength *= 3

elif(luck == 2):
    print(name1 + " is a Wizard")
    magic *= 3

else:
    print(name1 + " is a Potato")
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)


luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)
if(luck == 1):
    print(name2 + " is a Warrior")
    strength *= 3

elif(luck == 2):
    print(name2 + " is a Wizard")
    magic *= 3

else:
    print(name2 + " is a Potato")
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)


luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)
if(luck == 1):
    print(name3 + " is a Warrior")
    strength *= 3

elif(luck == 2):
    print(name3 + " is a Wizard")
    magic *= 3

else:
    print(name3 + " is a Potato")
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)


luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)
if(luck == 1):
    print(name4 + " is a Warrior")
    strength *= 3

elif(luck == 2):
    print(name4 + " is a Wizard")
    magic *= 3

else:
    print(name4 + " is a Potato")
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)


luck = random.randint(1,3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)
if(luck == 1):
    print(name5 + " is a Warrior")
    strength *= 3

elif(luck == 2):
    print(name5 + " is a Wizard")
    magic *= 3

else:
    print(name5 + " is a Potato")
    health *= 3

print("Strength:", strength)
print("Magic:", magic)
print("Health:", health)




