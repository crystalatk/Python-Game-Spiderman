from classes_interactions import Building, Option, Mob
from classes_spiderman import Spiderman

# importing "random" for random operations 
import random

# import to clear screen
from subprocess import call 
import os 

def clear(): 
    call('clear' if os.name =='posix' else 'cls') 

clear() 

# Buildings Instantiation
home = Building("home", 5, -10)
school = Building("school", -5, 5)
bus = Building("the bus", -5, 5)
park = Building("the park", 5, -5)

# Characters Instantiation
aunt_may = Mob("Aunt May", 5, -5, home, 2,  -10, ["You're late?!? I thought that you could sense the time, with your Peter-tingle.", "You know what? You should pack your suit, just in case. I have a tingle about it."] )

ned = Mob("Ned", -5, 5, home, 2, 5, ["Oh man, we are in so much trouble....", "Oh man, I'm so glad you are here!"])

mj = Mob("MJ", 5, -10, school, 1, 10, ["You know Suzanne Yang thinks that you’re a male escort?", "What is it with you and Spider-Man?"])

tony_stark = Mob("Tony Stark", 10, -15, park, 1, 20, ["Don't do anything I would do, and definitely don't do anything I wouldn't do. There's a little gray area in there, and that's where you operate.", "If You’re Nothing Without That Suit, Then You Shouldn't Have It."])

flash_thompson = Mob("Flash Thompson", 0, 20, school, 1, -5, ["I post stupid videos daily for people to like me!", "Penis Parker"], "Penis Parker")

happy = Mob("Happy", -5, 10, park, 2, -5, ["Heads up, Nick Fury is calling you.", "The one thing that Tony did that he didn’t second-guess was picking you."], "Parker")

good_thing_1 = Mob("Child with pregnant mom", 15, -10, bus, 1, 10, ["You're amazing!, just like Spider-Man!", "You suck!"], "Spider-Man")

quentin_beck = Mob("Quentin Beck", -15, 10, bus, 2, -10, ["I don’t think you know what’s real, Peter. You need to wake up! I mean, look at yourself. You are just a scared little kid in a sweatsuit! I", "You’ll see, Peter. People, they need to believe. And nowadays, they’ll believe anything."], "Night_Monkey")

# Options Instantiation
late = Option('late', 5, -5, home, 1, ["Wake up on-time", "Wake up late"])

dinner = Option("dinner", 5, -15, home, 2, ["come in five minutes late for dinner", "make dinner for Aunt May"])

room = Option("room", 5, -20, home, 1, ["clean your room", "wash your spidey suit in hot water"])

forgot_homework = Option("hw", 5, -15, school, 2, ["Forget your Homework", "Finish all your work"])

sat_in_gum = Option("gum", 5, -10, school, 2, ["sit in gum", "look before you sit"])

silly = Option("silly", 10, -20, school, 1, ["make a jake that landed", "trip in front of MJ"])

poo = Option( "poo", 10, -15, park, 1, ["decide to rent a bike", "step in dog poo"])

ice_cream = Option("desert", 5, -5, park, 2, ["buy a frozen lemonade", "buy an icecream cone"])

litter_patrol = Option("litter", 5, -10, park, 1, ["pick up the piece of garbage on teh ground", "walk past the garbage, you have bigger plans today!"])

helping_hand = Option("helping", 5, -10, bus, 1, ["help an old lady cross the street", "jaywalk"])

change = Option("change", 5, -5, bus, 2, ["search your pockets in vain, no change for the bus!", "remember to bring your bus pass! Got it!"])

kindness = Option("kindness", 10, -20, bus, 1, ["give up your seat for the pregnant mom of three", "listen to your music and play on your phone"])


# Setting variables: if I update any buildings, options, or mobs, these must be updated!
mobs_list = [aunt_may, mj, ned, happy, tony_stark, quentin_beck, flash_thompson, good_thing_1]

options_list = [late, dinner, room, forgot_homework, sat_in_gum, silly, poo, ice_cream, litter_patrol, helping_hand, change, kindness]

buildings_list = [home, school, bus, park]

level_multiplier = 1

# Defining common variables
result = ""

current_location = home

error_message = "Choose a number that matches a choice!"

# Set up Function to Print Menu for the Mobs and Location (Options is done within the class so I can practice calling a method within the class and because they print a phrase...)
def print_menu(temp_list, curr_set):
    print(curr_set.script)
    for idx, item in enumerate(temp_list):
        print(f"{idx+1}. {item.name}")
    while_break = True
    while while_break:
        try:
            user_choice = int(input("****Choose one: *****\n")) - 1
            if user_choice <= len(temp_list) - 1 and user_choice >=0:
                while_break = False
            else:
                raise ValueError
        except ValueError:
            print(error_message)
    current_item = temp_list[user_choice]
    return [current_item, user_choice] #For mobs, we need this list. 

# Spiderman Instantiation
spidey = Spiderman()



# ****Game Play Begins******
print("""              
           __                        O$               
       _.-'  )                        $'              
    .-'`. .-":        o      ___     ($o              
 .-'.-  .'   ;      ,st+.  .' , \    ($               
:_..-+""    :       T   "^T==^;\;;-._ $\              
\''''''\-,   ;       '    /  `-:-// / )$\             
        :   ;           /   /  :/ / /dP               
        :   :          /   :    )^-:_.l               
        ;    ;        /    ;    `.___, \           .-,
       :     :       :  /  ;.q$$$$$$b   \$$$p,    /  ;
       ;   :  ;      ; :   :$$$$$$$$$b   T$$$$b .'  / 
       ;   ;  :      ;   _.:$$$$$$$$$$    T$$P^"   /l 
       ;.__L_.:   .q$;  :$$$$$$$$$$$$$;_   TP .-" / ; 
       :$$$$$$;.q$$$$$  $$$$$$$$$$$$$$$$b  / /  .' /  
        $$$$$$$$$$$$$;  $$$$$$$$P^" "^Tb$b/   .'  :   
        :$$$$$$$$$$$$;  $$$$P^jp,      `$$_.+'    ;   
        $$$$$$$$$$$$$;  :$$$.d$$;`- _.-d$$ /     :    
        '^T$$$$$P^^"/   :$$$$$$P      d$$;/      ;    
                   :    $$$$$$P"-. .--$$P/      :     
                   ;    $$$$P'( ,    d$$:b     .$     
                   :    :$$P .-dP-'  $^'$$bqqpd$$     
                    `.   "" ' s")  .'  d$$$$$$$$'     
                      \           /;  :$$$$$$$P'      
                    _  "-, ;       '.  T$$$$P'        
                   / "-.'  :    .--.___.`^^'          
                  /      . :  .'                      
                  ),sss.  \  :  SPIDER-MAN                   
                 : TP""Tb. ; ;                        
                 ;  Tb  dP   :                        
                 :   TbdP    ;                        
                  \   $P    /                         
                   `-.___.-'
    """)

print(f"\nWelcome to the choose your own adventure Spider-Man game!\nIn this game, you want to achieve Hero status by getting 100 Hero points!\nBut be careful, too much stress (stess level > 100) or too low health (health = 0), will end your story!\n\nGet ready to have an amazing day!\n\n")

spidey.end_game_check()

while spidey.hero_status < 100 and spidey.stress_lvl < 100 and spidey.health > 0:#Game play loop. This loop ends when game play parameters are met
    
    associated_mobs = [] #This creates a list of mobs at the locations we chose
    associated_options = []#This creates a list of options at the location we chose
    temp_build_list = []#This creates the list of buildings a user can choose from each round. We are taking out the current building.
    
    # These for loops will add the options, mobs, and locationss that are associated with the current location
    for option_item in options_list:
        if option_item.location.name == current_location.name:
            associated_options.append(option_item)
    for mob_item in mobs_list:
        if mob_item.location.name == current_location.name:
            associated_mobs.append(mob_item)
    for loc_item in buildings_list:
        if current_location != loc_item:#We are removing the current building from the list. You can't go home if you are already home.
            temp_build_list.append(loc_item)

     # ***User Chooses their Option*** 
    current_option_number = random.randrange(0, len(associated_options) -1, 1) #This will give me a random option each time. Within the parenthesis (start, end, incriments)     
    curr_option = associated_options[current_option_number]  #This will give us a randomly picked option from the options available at this location. The user will continue to have new experiences.    
    
    print(f"Looks like you are at {current_location.name}. Now that you are here, you've got some choices to make. If they are good, it will increase your health. These choices might even make people happier to see you!\n")
    curr_option.print_script()

    while_break = True
    while while_break:
        try:
            user_choice_option = int(input("Please choose: \n"))
            if user_choice_option == 2 or user_choice_option ==1:
                while_break = False
            else:
                print(error_message)
        except ValueError:
            print(error_message)

    clear()

    if user_choice_option == curr_option.positive_choice:
        spidey.adjust_lvl_positive_choice(curr_option, level_multiplier)
        print("\nAmazing!\nGood choices now may result in some hero points later...")
        user_positive = True

    else: #If things go negatively!
        spidey.adjust_lvl_negative_choice(curr_option, level_multiplier)
        print("\nOh man!\nI hope these bad choices don't hurt you later.")
        user_positive = False

    if spidey.end_game_check():
        break
     
    # ***User chooses their Person to Interact with:***
    print(f"\n\nThose earlier choices looked like they affected your health and your stress levels. But the real goal is getting those Hero points!\nLet's see if we can find the right person to help Peter Parker become a true Hero!")

    current_list = print_menu(associated_mobs, mj) # I use MJ here, but any mob would work...
    current_mob = current_list[0]
    curr_number = current_list[1] + 1

    clear() 

    if user_positive: #this ties the person's phrase to the option the user chose earlier
        spidey.adjust_lvl_positive_choice(current_mob, level_multiplier)
        result = "Amazing! You are moving up in the world!"   
    else: #If things go negatively!
        spidey.adjust_lvl_negative_choice(current_mob, level_multiplier)
        result = ""
    print(f"\n\n\"{current_mob.phrase[current_list[1]]}\" --{current_mob.name} \n\n{result}")

    if spidey.end_game_check():
        break

        # ***User chooses a new location***
    current_list = print_menu(temp_build_list, current_location)
    current_location = current_list[0]
    spidey.adjust_lvl_positive_choice(current_list[0], level_multiplier)

    clear() 

    print(f"\n\nWelcome to {current_location.name}. I hope you have good luck here and an amazing day! Remember, you need 100 Hero Points to win!\nAs a special trick, some of your stats are tied to the location you choose.\nGet ready to have an amazing day!")

    if spidey.end_game_check():
        break
    
    level_multiplier += 1

# Win or lose statements
if spidey.hero_status >= 100:
    print("\n\nYou did it! You are a hero and an Avenger!\nCongratulations!!!")
else:
    print("\n\nYou made some bad choices, Spider-Man. You lose!")
