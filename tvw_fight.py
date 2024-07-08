"""
Module for the functions of the fight
- 
"""

from tvw_dices import user_D6, user_D20, enemy_D6, enemy_D20
from simple_colors import *
from tvw_healthbar import HealthBar, HealthBar_Enemy

# create an enemy character

wyrm = {
        "race" : "wyrm",
        "class" : "fighter",
        "hit points" : 20,
        "armor_class" : 10,
        "weapon" : "tale",
        "initiative bonus" : 1,
        "attack bonus" : 1,
        "damage" : 2,
}

# function for user's attack

def user_attack(user_D20, user_D6, user):
    user_attack = user_D20() + user["attack bonus"]
    if user_attack >= wyrm["armor_class"]:
        print(blue("Your attack was successful! Roll for damage."))
        user_damage = user_D6(user)
        ... # attack succeeds, deal damage
        wyrm["hit points"] -= user_damage
    else:
        print(red("Your attack failed! The wyrm will attack you now."))
    return wyrm["hit points"]

def enemy_attack(enemy_D20, enemy_D6, user):
    enemy_attack = enemy_D20() + wyrm["attack bonus"]
    if enemy_attack >= user["armor_class"]:
        print(red("The enemy attack was successful!"))
        enemy_damage = enemy_D6(wyrm) + wyrm["damage"]
        ... # attack succeeds, deal damage
        user["hit points"] -= enemy_damage  # maybe add a healthbar?
    else:
        print(blue("The enemy attack failed!"))
    return user["hit points"]

# function for wyrm's attack

# function for fight
def fight(user, enemy, character_name):
    user_intiative = user_D20() + user["initiative bonus"]
    wyrm_initiative = enemy_D20() + wyrm["initiative bonus"]
    enemy = wyrm

    user_healthbar = HealthBar(user, color="green")
    enemy_healthbar = HealthBar_Enemy(enemy)


    if user_intiative >= wyrm_initiative: # the user attacks first 
        print(blue("You attack first! Roll for an attack."))
        attacker = user
    else: # the wyrm attacks first
        print(red("The Wyrm attacks first, brace yourself!"))
        attacker = enemy

    while user["hit points"] > 0 and enemy["hit points"] > 0:
        if attacker == user:
            user_attack(user_D20, user_D6, user)
            attacker = enemy
        else:
            enemy_attack(enemy_D20, enemy_D6, user)
            # Update and draw health bars
            user_healthbar.update()
            enemy_healthbar.update()
            user_healthbar.draw()
            enemy_healthbar.draw()
            if user["hit points"] <= 0:
                print(f"{character_name}, you are mortally wounded.")
            else:
                #print(f"{character_name}, you have {user["hit points"]} hit points left.\n")
                print(blue(f"{character_name}, now it's your turn to attack!"))
            attacker = user

    if user["hit points"] <= 0:
        print(red("The Wyrm lands it's final blow and you are defeated! ", ["reverse"]))
    else: 
        print(green("You land your final blow on the Wyrm and hear a terrible screach as it dies.", ["reverse"]))
        print(f"'{character_name}!' You hear a tearful voice. 'You have defeated the Wyrm! Thank you for rescuing me!'")
        print(f"Behind the dead body of the Wyrm, you see your friend Dayereth.\nHappy end.")

        