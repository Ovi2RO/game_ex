import random

player = 0
cpu = 0

print("Win 3 to win the game!!!")

while player < 3 and cpu < 3:
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = input("Rock, Paper or Scissors: ")
    print(f"CPU: {cpu_choice}\nPlayer: {player_choice}")

    if player_choice.lower() == cpu_choice:
        print("Tie!!!")
    elif player_choice.lower() == "rock":
        if cpu_choice == "scissors":
            player +=1
            print("Player wins")
        else:
            cpu += 1
            print("CPU wins")
    elif player_choice.lower() == "paper":
        if cpu_choice == "rock":
            player +=1
            print("Player wins")
        else:
            cpu += 1
            print("CPU wins")
    elif player_choice.lower() == "scissors":
        if cpu_choice == "paper":
            player +=1
            print("Player wins")
        else:
            cpu += 1
            print("CPU wins")
    else:
        print("Invalid input")

if player > cpu:
    print("Player wins!!!")
else:
    print("CPU wins!!!")
