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
import tvw_charcreation 

with open("dwarf.txt", encoding='utf-8') as descr_file:
        content = descr_file.read().replace("\n", " ")
        return character_name, content