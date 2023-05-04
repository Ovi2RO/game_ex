import random

player = input("Welcome to casino Py! What is your name? \n>")
password = input("What is the secret password? \n>")

if(password.lower() != "secret"):
    print("What? The packing lot is closed!")
else:
    roll = input("Type roll to roll: ")
    lucky = random.randint(0, 10)

    if(roll.lower() == "roll"):
        number = random.randint(0, 10)
        if(lucky > number):
            print(f"Your number is {number}, my number is {lucky}")
            print("I win!!!")
        elif(number > lucky):
            print(f"Your number is {number}, my number is {lucky}")
            print(f"{player} wins!!!")
        else:
            print(f"Your number is {number}, my number is {lucky}")
            print("We both win! And we both lost!!!")
    else:
        print("You don't want to play! Bye!")



