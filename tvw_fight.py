"""
Module for the functions of the fihgt
- 
"""

from tvw_dices import user_D6, user_D20, enemy_D6, enemy_D20
from tvw_charcreation import characters, char_choice

# create an enemy character

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

# function for user's attack

def user_attack(user_D20, user_D6):
    user_attack = user_D20 + characters[char_choice]["attack bonus"]
    health_wyrm = wyrm["hit points"] # this probably restarts the hit points
    if user_attack >= wyrm["armor_class"]:
        print(f"Your attack was successful!")
        user_D6()
        ... # attack succeeds, deal damage
        health_wyrm -= user_damage
    else:
        print(f"Your attack failed!")
    return health_wyrm


# function for wyrm's attack

# function for fight
def fight(user, enemy):
    user_intiative = user_D20 + characters[char_choice]["initiative bonus"]
    wyrm_initiative = enemy_D20 + wyrm["initiative bonus"]
    if user_intiative >= wyrm_initiative: # the user attacks first 
        print(f"You attack first!")
        attacker, defender = user, enemy
    else: # the wyrm attacks first
        print(f"The Wyrm attacks first, brace yourself!")
        attacker, defender = enemy, user

    while user[]
