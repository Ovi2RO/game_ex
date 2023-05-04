import random
import os
import time

colors = "RGBY"
simon = ""

for score in range(0, 10):
    simon += random.choice(colors)
    for color in simon:
        print(color)
        time.sleep(1.5)
        os.system("clear")
    guess = input("Repeat: ")
    os.system("clear")
    if guess != simon:
        break

print(f"Game over! Your final score is {score}")
