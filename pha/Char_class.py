import random


class Char_class:
    def c_class():
        char_class = ""
        char_class_pos = random.randint(1, 3)
        if(char_class_pos == 1):
            char_class = "Barbarian"
        elif(char_class_pos == 2):
            char_class = "Cleric"
        else:
            char_class = "Druid"
        return char_class