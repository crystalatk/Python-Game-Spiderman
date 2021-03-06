class Building:
    def __init__(self, name, health_imp, stress_lvl_imp, object_type="buildings", script="It's time to move! Where would you like to go? Remember, a place can really affect your well-being..."):
        self.name = name
        self.health_imp = health_imp
        self.stress_lvl_imp = stress_lvl_imp
        self.object_type = object_type
        self.script = script

class Option(Building):#change to options!
    def __init__(self, name, health_imp, stress_lvl_imp, location, positive_choice, phrase, object_type="option", script="****Do you...**** "):
        super().__init__(name, health_imp, stress_lvl_imp, object_type, script)
        self.location = location
        self.phrase = phrase
        self.positive_choice = positive_choice
    
    def print_script(self): #Prints Options menu
        print(self.script)
        for idx, item in enumerate(self.phrase):
            print(f"{idx+1}. {item}")
        # super().print_script(self)

class Mob(Option):
    def __init__(self, name, health_imp, stress_lvl_imp, location, positive_choice, hero_status_imp, phrase, nickname="Peter"):
        super().__init__(name, health_imp, stress_lvl_imp, location, positive_choice, phrase, "people", "Spidey sense is kicking in!\n****Who do you want to talk to? ****")
        self.hero_status_imp = hero_status_imp
        self.nickname = nickname
        # super().print_script(self)





