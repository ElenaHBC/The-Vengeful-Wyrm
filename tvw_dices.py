"""
Module for the different functions for the different dices
- D20: for initiative, attack and skill checks
- D6: for damage
"""

import random

# D6: dice with 6 sides
def D_6():
    d6 = random.randrange(1, 7)
    return d6

# D20: dice with 20 sides
def D_20():
    d20 = random.randrange(1, 21)
    return d20

print(D_6())
print(D_20())