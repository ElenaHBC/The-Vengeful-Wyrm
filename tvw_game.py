"""
Create a game function to:
- give intro
- initiate the game
- go trough the story
- rotate between attacks during battle
- offer possibility to play again
"""

import random
from tvw_charcreation import characters, choose_character, name_character, char_choice
from tvw_dices import user_D6, user_D20, enemy_D6, enemy_D20
from tvw_mission import mission, mission_decision

play_again = input("Do you want to play again? yes/no: ")

def the_vengeful_wyrm():
    with open("intro.txt", encoding='utf-8') as intro_file: # starting the game with a short intro about it
        content = intro_file.read().replace("\n", " ")
        return content # code undearneath unreachable because of return statement 
    
    if mission() == "yes":
        path = choose_path()
    mission_decision()

    
    # defining some variables, so the code is more clean
    char_choice = choose_character(characters)
    character_name = name_character()
    character_description = descr_character(char_choice)
    user = characters[char_choice]

    while play_again == "yes": #this would be for playing again, but we need to initialize the first game
       
        
the_vengeful_wyrm()