"""
Module for the functions of the fihgt
- 
"""

from tvw_dices import user_D6, user_D20, enemy_D6, enemy_D20
from tvw_charcreation import characters, choose_character, name_character


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
    user_attack = user_D20() + user["attack bonus"]
    if user_attack >= wyrm["armor_class"]:
        print("Your attack was successful!")
        user_damage = user_D6()
        ... # attack succeeds, deal damage
        wyrm["hit points"] -= user_damage
    else:
        print("Your attack failed!")
    return wyrm["hit points"]

def enemy_attack(enemy_D20, enemy_D6):
    enemy_attack = enemy_D20() + wyrm["attack bonus"]
    if enemy_attack >= user["armor_class"]:
        print("The enemy attack was successful!")
        enemy_damage = enemy_D6()
        ... # attack succeeds, deal damage
        user["hit points"] -= enemy_damage
    else:
        print("The enemy attack failed!")
    return user["hit points"]

# function for wyrm's attack

# function for fight
def fight(user, enemy):
    user_intiative = user_D20() + characters[char_choice]["initiative bonus"]
    wyrm_initiative = enemy_D20() + wyrm["initiative bonus"]

    if user_intiative >= wyrm_initiative: # the user attacks first 
        print(f"You attack first!")
        attacker = user
    else: # the wyrm attacks first
        print(f"The Wyrm attacks first, brace yourself!")
        attacker = enemy

    while user["hit points"] > 0 and enemy["hit points"] > 0:
        if attacker == user:
            user_attack(user, enemy)
            attacker = enemy
        else:
            enemy_attack(user, enemy)
            attacker = user

    if user["hit points"] <= 0:
        print("The Wyrm land it's final blow and you are defeated! ")
    else: 
        print("You land your final blow on the Wyrm and hear a terrible screach as it dies.")
        print(f"'{character_name}!' You hear a tearful voice. 'You have defeated the Wyrm! Thank you for rescuing me!'")
        print(f"Behind the dead body of the Wyrm, you see your friend Dayereth.")

        