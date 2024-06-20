"""
Module for the choice of the path
- obstacle river on the way, choose wisdom or strength path
- wisdom way is crossing the river over the bridge with a troll who gives a riddle
- strength way is swimming through the river and making a skill check
"""

from tvw_dices import user_D20


def choose_path():
    while True:
        print("You see a river blocking your way. To cross the river you have to choose between two paths.")
        print("."*20)
        path = input("Do you choose the path of wisdom or the path of strength? (wisdom/strength): ").lower()
        if path in ["wisdom","strength"]:
            return path
        else:
            print("This is not a valid response. Please choose either 'wisdom' or 'strength'.")

def riddle(character_name):
    print(f"You chose the path of wisdom, {character_name}. You see a bridge over the river and proceed to cross it.")
    print("As you come to the bridge you see a troll who demands a toll. *badumts*")
    print("."*20)
    print("Hello there, traveler! I see ya want to cross me bridge! I've to check if you are worthy! Answer this riddle for me, will ya.")
    riddle_answer = input("What is always in front of you but can't be seen?: ").lower()
    if riddle_answer in ["the future", "future"]:
        print("You're some clever traveler! I don't see your future, but I'm sure it is full of adventures! You may proceed.")
        return True
    else: 
        print("Well, well, well... Another muttonheaded traveler on the road. You are not worthy of crossing my mighty bridge! ")
        # offer the choice of strength of fighing the troll, of just end the game and try again?
        return False

def river(character_name, user): 
    print(f"You chose the path of strength, {character_name}. You make you way to the river and proceed to swim through it.")
    print("To do that you need to make a skill check and roll a D20.")
    skill_check = user_D20()
    if skill_check + user["athletics"] > 10: # skill check succeeds
        print(f"With your athletics modifier of +{user["athletics"]} is your total {skill_check + user["athletics"]}. Success!")
        print("You are a skillful master of the water and glide through it like a fish.")
        return True
    else: # skill check fails
        print(f"With your athletics modifier of +{user["athletics"]} is your total {skill_check + user["athletics"]}. This fails!")
        print("The river is violent this time of the year. You try to swim, but the current sweeps you away.")
        print("Your armor drags you down and you drown.") 
        return False

