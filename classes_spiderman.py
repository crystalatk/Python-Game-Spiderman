class Spiderman:
    def __init__(self):
        self.name = "Spider-man"
        self.health = 70
        self.stress_lvl = 10
        self.hero_status = 0
        print(f"\n\nYou have been bit by a radioactive spider and now you are {self.name.upper()}!!!")
    
    def adjust_lvl_positive_choice(self, choice, multiplier):
        self.health += choice.health_imp * multiplier
        if self.health > 100:
            self.health = 100
        self.stress_lvl += choice.stress_lvl_imp * multiplier
        if self.stress_lvl < 0:
            self.stress_lvl = 0
        if choice.object_type == "people":
            self.hero_status += choice.hero_status_imp * multiplier
            if self.hero_status < 0:
                self.hero_status = 0
        
    def adjust_lvl_negative_choice(self, choice, multiplier):
        self.health -= choice.health_imp * multiplier
        self.stress_lvl -= choice.stress_lvl_imp * multiplier
        if self.stress_lvl < 0:
            self.stress_lvl = 0
        if choice.object_type == "people":
            self.hero_status += choice.hero_status_imp * multiplier#the people you interact with always affect your hero status the same way, even if your earlier choices were negative...
            if self.hero_status < 0:
                self.hero_status = 0

    def end_game_check(self):
        print(f"\n\n****Your current stats**** \nHealth: {self.health}\nStress Level: {self.stress_lvl}\nHero Points: {self.hero_status}\n\n")
        if self.hero_status >= 100 or self.health <=0 or self.stress_lvl >= 100:
            return True
        else:
            return False