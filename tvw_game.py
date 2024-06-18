"""
Create a game function to:
- give intro
- initiate the game
- go trough the story
- rotate between attacks during battle
- offer possibility to play again
"""

from tvw_charcreation import game_intro, characters, choose_character, name_character, descr_character
from tvw_mission import mission, mission_decision
from tvw_path import choose_path, riddle, river
from tvw_fight import fight

# defining some variables, so the code is more clean

def the_vengeful_wyrm():
    print(game_intro())
    print("Please choose a character from the following list: ")

    char_choice = choose_character(characters)
    character_name = name_character()
    character_description = descr_character(char_choice, character_name)
    print(character_description)
    user = characters[char_choice]
        
    if mission(character_name) == "yes" or mission_decision(mission, character_name) == True:
        with open("mission_accept.txt", encoding='utf-8') as mission_accept_file: 
            content = mission_accept_file.read().replace("\n", " ")
            print (content)
        path = choose_path()
        if path == "wisdom":
            riddle(character_name)
        else:
            river(character_name)

    else:
        print("By declining the mission you decided not to play this game. This is disapointing.")
        exit()

        
the_vengeful_wyrm()
