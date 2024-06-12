# The-Vengeful-Wyrm

"The Vengeful Wyrm" is a DnD text based mini game planned as a final project for the [PyLadies Course 2024 in Vienna](https://pyladies.at/2024/pyladies-en-vienna-2024-spring/). 

The game will include different coding concepts learned throughout the course. 
Some of them are:
- loops
- custom functions
- Git/GitHub
- dictionaries 
- handling exceptions
- modules
- reading files
- APIs

## Game flow

The game will start with short greetings and description. The user will be then prompted to choose a character from predefined options. The predefined character options will be stored as dictionaries. If the user wants to know more about the characters, a detailed description will be then recalled/read from a text file. Maybe an image of the character will be included through APIs. The user will be then prompted to give a name to the character (isalpha() check to see if the name is reasonable) and the brave new adventurer will be greated and confronted with the information of the kidnaped friend. The user will then have the option to go save the friend or to do nothing (and then finding out either that the friend dies and be conscience-stricken till the rest of time, maybe also haunted by the ghost), or 1 day later plagued by guilty conscience and guilt-ridden going on the mission to save the friend. 

If the user chooses the adventure, the journey will be described and there would be a choice of 2 ways.
Depending on the choice of the user, a different enemy will show on the way and a fight will take place. Rolling for initiative (random D20 + initiative bonus), rolling for attacks + damage untill the user either wins or loses against the enemy.

A short epilogue will follow describing the glorious victory or the terrible defeat.

The user will then have a choice to either start over and play again or end the game.

```mermaid
flowchart TD
    A[Greetings] -->|Choose character| B(Give name) 
    B --> |detailed character description y/n| C[Scenery and mission description]
    C --> |mission yes| D[adventure]
    C -->|mission no| E[guilty conscience]
    E --> |end game| F[haunted end]
    E --> |start over| C
    D --> |long or short way| G[journey description]
    G --> H[enemy 1]
    G --> I[enemy 2]
    H --> J[fight]
    I --> J
    J --> K[win] --> |Hooray, play again? no| M[end]
    K --> |Hooray, play again? yes| A
    J --> L[lose] --> |Boo, play again? no| M
    J --> |Boo, play again? yes| A
```