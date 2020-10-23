class Buildings:
    def __init__(self, name, health_imp, stress_lvl_imp, object_type="buildings", script="Time to move on! Where would you like to go now?"):
        self.name = name
        self.health_imp = health_imp
        self.stress_lvl_imp = stress_lvl_imp
        self.object_type = object_type
        self.script = script

    # def print_script(self, curr_location): #Prints buildings menu
       
    #     print(self.script)
    #     for idx, item in enumerate(buildings_list.name):
    #         if self.buildings_list != curr_location:
    #             print(f"{idx+1}. {item}")



class Options(Buildings):#change to options!
    def __init__(self, name, health_imp, stress_lvl_imp, location, positive_choice, phrase, object_type="option", script="Do you... "):
        super().__init__(name, health_imp, stress_lvl_imp, object_type, script)
        self.location = location
        self.phrase = phrase
        self.positive_choice = positive_choice
    
    def print_script(self): #Prints Options and Mobs menu
        print(self.script)
        for idx, item in enumerate(self.phrase):
            print(f"{idx+1}. {item}")
        # super().print_script(self)

class Mobs(Options):
    def __init__(self, name, health_imp, stress_lvl_imp, location, positive_choice, hero_status_imp, phrase, nickname="Peter"):
        super().__init__(name, health_imp, stress_lvl_imp, location, positive_choice, phrase, "people", "Spidey sense is kicking in! Who do you want to talk to?")
        self.hero_status_imp = hero_status_imp
        self.nickname = nickname
        # super().print_script(self)





