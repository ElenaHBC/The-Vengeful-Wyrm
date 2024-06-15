"""
Create a game function to:
- give intro
- initiate the game
- go trough the story
- rotate between attacks during battle
- offer possibility to play again
"""

import random
import tvw_charcreation, tvw_dices, tvw_mission

play_again = input("Do you want to play again? yes/no: ")

def the_vengeful_wyrm():
    while play_again == "yes":
        with open("intro.txt", encoding='utf-8') as intro_file:
            content = intro_file.read().replace("\n", " ")
            return content
        
the_vengeful_wyrm()