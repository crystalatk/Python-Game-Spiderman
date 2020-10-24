from classes_interactions import Buildings
from classes_interactions import Mobs
from classes_interactions import Options

class Spiderman:
    def __init__(self):
        self.name = "Spider-man"
        self.health = 70
        self.stress_lvl = 10
        self.hero_status = 0
        print(f"\n\nYou have been bit by a radioactive spider and now you are {self.name.upper()}!!!")
    
    def adjust_lvl_positive_choice(self, choice):
        self.health += choice.health_imp
        self.stress_lvl += choice.stress_lvl_imp
        if self.stress_lvl < 0:
            self.stress_lvl = 0
        if choice.object_type == "people":
            self.hero_status += choice.hero_status_imp
            if self.hero_status < 0:
                self.hero_status = 0
        
    def adjust_lvl_negative_choice(self, choice):
        self.health -= choice.health_imp
        self.stress_lvl -= choice.stress_lvl_imp
        if self.stress_lvl < 0:
            self.stress_lvl = 0
        if choice.object_type == "people":
            self.hero_status += choice.hero_status_imp #the people you interact with always affect your hero status the same way, even if your earlier choices were negative...
            if self.hero_status < 0:
                self.hero_status = 0
