import random


class Char_stat:
    
    def c_strength(self, ch_class):
        self.char_class = ch_class
        char_strength = random.randint(3, 15)
        if(ch_class == "Barbarian"):
            char_strength *= 3 
        return char_strength

    def c_health(self, ch_class):
        self.char_class = ch_class
        char_health = random.randint(3, 15)
        if(ch_class == "Barbarian"):
            char_health *= 3
        elif(ch_class == "Druid"):
            char_health *= 2
        return char_health
    
    def c_magic(self, ch_class):
        self.char_class = ch_class
        char_magic = random.randint(3, 15)
        if(ch_class == "Cleric"):
            char_magic *= 3
        elif(ch_class == "Druid"):
            char_magic *= 2
        return char_magic
    
    def c_initiative(self, ch_class):
        self.char_class = ch_class
        char_initiative = random.randint(3, 15)
        if(ch_class == "Cleric"):
            char_initiative *= 3
        elif(ch_class == "Druid"):
            char_initiative *= 2
        return char_initiative


        
            
    


        

    
        