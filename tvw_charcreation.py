"""
Creating a custom module DND_tvw with the functions needed for the game.

Separate functions for:
- choosing character from predefined list/dict while loop
- giving name to the character while loop
- learning details about the character + read file

- saving the friend if else function
- choosing a way while(if else)
- short way riddle (like password func), 2 guesses while / or incorporate hangman style riddle
- long way swimming if else (difficulty class of the river)
- initiative roll - separates for user and enemy?
- attack roll - separates for user and enemy?
- game function - while loop untill end 

Should all of these functions be in different modules for better overview?

"""

# Function for choosing a character: 
# short description, saving the choice 

from simple_colors import *
from tvw_charimage import display_image, dwarf_img, elf_img, wizzard_img

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


def choose_character(characters):
    choices = ["first", "second", "third", "1", "2", "3"]
    #print("Please choose a character from the following list: ") #remove the printing statements from the functions
    for char_num, char_inf in characters.items():
        description = (
            f"{char_num.capitalize()} option is a {char_inf['race']} {char_inf['class']} "
            f"with {char_inf['hit points']} hit points and an armor class of {char_inf['armor_class']}. "
            f"They wield a {char_inf['weapon']} with an attack bonus of {char_inf['attack bonus']} and "
            f"deal {char_inf['damage']} damage. Their initiative bonus is {char_inf['initiative bonus']} and "
            f"they have an athletics skill of {char_inf['athletics']}."
        )
        print(description)
        print()
    while True: 
        char_choice = str(input("To choose a character, please write first, second or third, accordingly: ")).lower()
        if char_choice in choices:
            if char_choice == "1":
                return "first"
            elif char_choice == "2":
                return "second"
            elif char_choice == "3":
                return "third"
            else:
                return char_choice
        else:
            print("This is not an option.")
        
# Function for naming the character: 
# naming the character, giving a detailed description of the character?

def name_character():
    while True:
        name = input("Please give a name to your character: ").capitalize()
        if name.isalpha():
            print(f"Greetings, {name}!")
            print()
            return name
        else:
            print("Please enter a name that contains only letters and no spaces.")

# Function for detailed description:

def descr_character(char_choice, character_name):
    print(yellow(f"{" Character's description ":*^40}"))
    if char_choice == "first":
        display_image(dwarf_img)
        with open("dwarf.txt", encoding='utf-8') as descr_file:
            content = descr_file.read().replace("\n", " ")
            return character_name, content
    elif char_choice == "second":
        display_image(elf_img)
        with open("elf.txt", encoding='utf-8') as descr_file:
            content = descr_file.read().replace("\n", " ")
            return character_name, content
    else:
        display_image(wizzard_img)
        with open("human.txt", encoding='utf-8') as descr_file:
            content = descr_file.read().replace("\n", " ")
            return character_name, content

# include the intro to the game in this module 

def game_intro():
    print(yellow(f"{" Welcome ":*^40}"))
    with open("intro.txt", encoding='utf-8') as intro_file: # starting the game with a short intro about it
        content = intro_file.read().replace("\n", " ")
        return content 
