"""
Module for the different functions for the different dices
- D20: for initiative, attack and skill checks
- D6: for damage

- separate function for rolling the dice and saving the outcome
- separate functions for the user and enemy
"""

from random import randint

""" User's dices """
# D6: dice with 6 sides

def user_D6():
    while True:
        roll = input("To roll a D6 dice type anything: ")
        if roll:
            user_d6 = randint(1, 6)
            print(f"You rolled a {user_d6}!")
            return user_d6
        else:
            print("You did not type anything, try again.")

user_D6()

# D20: dice with 20 sides
def user_D20():
    while True:
        roll = input("To roll a D20 dice type anything: ")
        if roll:
            user_d20 = randint(1, 20)
            print(f"You rolled a {user_d20}!")
            return user_d20
        else:
            print("You did not type anything, try again.")

user_D20()


""" Enemy's dices """
# D6: dice with 6 sides

def enemy_D6():
    enemy_d6 = randint(1, 6)
    print(f"The Wyrm rolled a {enemy_d6}!")
    return enemy_d6

enemy_D6()

# D20: dice with 20 sides
def enemy_D20():
    enemy_d20 = randint(1, 20)
    print(f"The Wyrm rolled a {enemy_d20}!")
    return enemy_d20

enemy_D20()