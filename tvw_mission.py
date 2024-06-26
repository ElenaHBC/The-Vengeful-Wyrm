"""
Create a module with functions for the mission:
- include a description of the situation: user's character is drinking ale 
- {character_name} + read file
- Thara storms in, wounded and teriffied, finds the user's character, tells the story of the kidnapping of Dayereth + read file
- if else function: accepting or declining to save Dayereth
- if no: are you sure - yes, read file with story of Dayereth's death, plagued by guilt and haunted
- if yes: read file with description of the way and choices
- function which short/long way
"""
import time
from simple_colors import *

# function for accepting mission or declining
def mission(character_name):
    print()
    print(yellow(f"{" Chapter One: Huge Shadow ":*^40}"))
    with open("mission.txt", encoding='utf-8') as mission_file:
        content = mission_file.read().replace("\n", " ")
        print (content, "\n")
    while True: 
        print("."*20)
        print(f"You have to save him, {character_name}! Please, will you help?")
        save_Dayereth = input("To answer, please type yes or no: ").lower()
        if save_Dayereth == "yes":
            print(f"'Thank you, {character_name}!' said Thara sighing in relief and overcomed by exhaustion, faints.\n ")
            time.sleep(0.5)
            return True
        elif save_Dayereth == "no":
            print(f"'I cannot believe my ears, {character_name}!' said Thara gasping in disbelief.\n")
            time.sleep(0.5)
            return False
        else:
            print(f"'I did not understand that, {character_name}!' Could you repeat?")


# function for outcome of the answer for the mission, uses the outcome of mission() func as argument
def mission_decision(mission_result, character_name):
        if mission_result == False:
            while True:
                ask_again = input(f"{character_name}, are you really sure?: ").lower()
                if ask_again == "yes":
                    with open("mission_decline.txt", encoding='utf-8') as mission_decline_file: #write a story about death and regret
                        content = mission_decline_file.read().replace("\n", " ")
                        print()
                        print(yellow(f"{" Chapter Two: Dark Promise ":*^40}"))
                        print (content)
                        return False # instead of break, so we can use this output/return for combination with other functions
                    
                elif ask_again == "no": # I am glad you changed your mind, read file way to forest
                    print(f"'I knew I could count on you, {character_name}!' said Thara sighing in relief and overcomed by exhaustion, faints.\n")
                    return True
                    
                else: # I do not understand, loop to the beginning
                    print(f"'I did not understand that, {character_name}!' Could you repeat?")
        else: 
            with open("mission_accept.txt", encoding='utf-8') as mission_accept_file:
                        content = mission_accept_file.read().replace("\n", " ")
                        print (content)
                        return True
