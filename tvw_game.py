"""
Create a game function to:
- give intro
- initiate the game
- go trough the story
- rotate between attacks during battle
- offer possibility to play again
"""

import random
from tvw_charcreation import characters, choose_character, name_character, descr_character, game_intro
from tvw_dices import user_D6, user_D20, enemy_D6, enemy_D20
from tvw_mission import mission, mission_decision
from tvw_path import choose_path, riddle, river

play_again = input("Do you want to try again? yes/no: ")

def the_vengeful_wyrm():
    game_intro()
    # defining some variables, so the code is more clean
    char_choice = choose_character(characters)
    character_name = name_character()
    character_description = descr_character(char_choice)
    user = characters[char_choice]
       
    if mission() == "yes" or mission_decision(mission) == True:
        path = choose_path()
        if path == "wisdom":
            riddle()
        else:
            river()

    else:
        print("By declining the mission you decided not to play this game. This is disapointing.")
            
        

    


    while play_again == "yes": #this would be for playing again, but we need to initialize the first game
       
        
the_vengeful_wyrm()