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
from tvw_charcreation import character_name

# function for accepting mission or declining
def mission():
    print("*"*20)
    with open("mission.txt", encoding='utf-8') as mission_file:
        content = mission_file.read().replace("\n", " ")
        print (content)
    while True: #this creates an endless loop
        print("."*20)
        print(f"You have to save him, {character_name}! Please, will you help?")
        save_Dayereth = input("To answer, please type yes or no: ")
        if save_Dayereth == "yes":
            print(f"'Thank you, {character_name}!' said Thara sighing in relief and overcomed by exhaustion, faints.")
            print(f"Your expression shifts from calm to determined. You rise swiftly to your feet and make your way to the forest.")
            break
        elif save_Dayereth == "no":
            print(f"'You are a terrible friend, {character_name}!' said Thara gasping in disbelief.")
            break
        else:
            print(f"'I did not understand that, {character_name}!' Could you repeat?")
    return save_Dayereth

# function for outcome of the answer for the mission

# function for the choice of the way

mission()