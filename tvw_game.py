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
    print(game_intro())
    print("Please choose a character from the following list: ")

    char_choice = choose_character(characters)
    character_name = name_character()
    character_description = descr_character(char_choice, character_name)
    print(character_description)
    user = characters[char_choice]
    enemy = wyrm
        
    if mission(character_name) == "yes" or mission_decision(mission, character_name) == True:
        with open("mission_accept.txt", encoding='utf-8') as mission_accept_file: 
            content = mission_accept_file.read().replace("\n", " ")
            print (content)
        path = choose_path()
        if path == "wisdom":
            riddle(character_name)
            if riddle(character_name) == True:
                fight(user, enemy, character_name)
            else: 
                print("The trolls eats you. Game over.")
                exit()
        else:
            river(character_name)
            if river(character_name) == True:
                fight(user, enemy, character_name)
            else: 
                print("You drown.")
                exit()
            

    else:
        print("By declining the mission you decided not to play this game. This is disapointing.")
        exit()

    if riddle(character_name) == True or river(character_name) == True:
        fight(user, enemy, character_name)

        
the_vengeful_wyrm()
