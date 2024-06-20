"""
Create a game function to:
- give intro
- initiate the game
- go trough the story
- rotate between attacks during battle
- offer possibility to play again
"""

from tvw_charcreation import game_intro, choose_character, name_character, descr_character
from tvw_mission import mission, mission_decision
from tvw_path import choose_path, riddle, river
from tvw_fight import fight

import time

characters = {
    "first" : {
        "race" : "dwarf",
        "class" : "fighter",
        "hit points" : 15,
        "armor_class" : 12,
        "weapon" : "battle axe",
        "initiative bonus" : 2,
        "attack bonus" : 3,
        "damage" : 2,
        "athletics" : 1
    },
     "second" : {
        "race" : "elf",
        "class" : "ranger",
        "hit points" : 13,
        "armor_class" : 10,
        "weapon" : "long bow",
        "initiative bonus" : 3,
        "attack bonus" : 3,
        "damage" : 2,
        "athletics" : 3
     },
     "third" : {
        "race" : "human",
        "class" : "wizzard",
        "hit points" : 12,
        "armor_class" : 11,
        "weapon" : "fire ball",
        "initiative bonus" : 4,
        "attack bonus" : 2,
        "damage" : 4,
        "athletics" : 2
     }
}

wyrm = {
        "race" : "wyrm",
        "class" : "fighter",
        "hit points" : 25,
        "armor_class" : 10,
        "weapon" : "tale",
        "initiative bonus" : 1,
        "attack bonus" : 1,
        "damage" : 2,
}


def the_vengeful_wyrm():
    print(game_intro(),"\n")
    time.sleep(1)
    print("*"*20 + " Choose your character " + "*"*20)
    time.sleep(1)
    print("Please choose a character from the following list: \n")
    time.sleep(1)

    char_choice = choose_character(characters)
    character_name = name_character()
    character_description = descr_character(char_choice, character_name)
    print(character_description)
    user = characters[char_choice]
    enemy = wyrm
    mission_result = mission(character_name)
        
    if mission_result == True or mission_decision(mission_result, character_name) == True:
        print("*"*20 + " Chapter Two: Right Path " + "*"*20)
        with open("mission_accept.txt", encoding='utf-8') as mission_accept_file: 
            content = mission_accept_file.read().replace("\n", " ")
            time.sleep(0.5)
            print (content)
        path = choose_path()
        if path == "wisdom":
            if riddle(character_name) == True:
                print("You make your way on the bridge and to the forest.")
                time.sleep(1)
                print("*"*20 + " Chapter Three: Wyrm's Lair " + "*"*20)
                with open("forest.txt", encoding='utf-8') as forest_file: 
                    content = forest_file.read().replace("\n", " ")
                    print (content)
                fight(user, enemy, character_name)
            else: 
                print("The trolls eats you. Game over.")
                exit()
        else:
            if river(character_name, user) == True:
                print("Once you are on the other side of the river you make your way to the forest.")
                time.sleep(1)
                print("*"*20 + " Chapter Three: Wyrm's Lair " + "*"*20)
                with open("forest.txt", encoding='utf-8') as forest_file: 
                    content = forest_file.read().replace("\n", " ")
                    print (content)
                fight(user, enemy, character_name)
            else: 
                print("Game over.")
                exit()
            

    else:
        print("\nBy declining the mission you decided not to play this game. This is disapointing.")
        exit()

play_again = "yes"

while play_again == "yes".lower():
    the_vengeful_wyrm()
    play_again = input("Do you want to play again? yes/no: ")
    if play_again == "no".lower():
        break
    else:
        print("I did not understand that, please answer with yes or no.")

